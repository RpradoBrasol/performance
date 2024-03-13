import glob
import os
import pandas as pd

user: str = os.path.expanduser('~')
n_rows_sgis: int = 24 ## Numero de linhas no csv do SGIS
# tilt: str = ''
errors: dict = {}
df_def = pd.DataFrame()

def name_extract(file):
    filename: str = file.replace("SolarGIS_hourly_", "").replace("Solargis_TS_hourly_", "").replace("_Brazil", "").replace("Brasol_", "").replace("SolarGIS_min15_", "").replace('-','').replace(' ','')     
    source: str = file.upper()
    for letter in filename:
        if letter.isnumeric():
            continue
        
        elif letter.isalpha and letter == "_":     
            # global tilt        
            tilt = filename[:filename.index(letter)] ## Arranjo da usina       
                            
        elif letter.isalpha and letter != "_":   
            filename = filename[filename.index(letter):]
            break  
    
    asset_name: str = filename[:-13].replace("_"," ").replace('-','').replace(' ', '').upper()
    return (asset_name, tilt, source)

def df_sgis(file):
    header_sgis: int = 53
    data_rows: int = 25
    if file[-12:-4].isnumeric() and file[-21:-13].isnumeric(): # CSVs enviados com o consolidado do mes anterior
        return None, None
    else:
        try:
            df = pd.read_csv(file, sep = ';', skiprows = header_sgis , on_bad_lines='skip', nrows= (header_sgis+data_rows))
            return df, None
        except pd.errors.EmptyDataError as e:
            return None, str(e)

def df_unit(df, project_name, project_tilt):
    drop_col = ['Time', 'GHI', 'DIF', 'DNI', 'GTI', 'SE', 'SA', 'TEMP', 'WS', 'WD']
    try:
        df_adj = df.drop(drop_col, axis = 1, errors = 'ignore')
        date_adj: str = df_adj.iloc[0,0][-4:] + '-' + df_adj.iloc[0,0][3:5] + '-' + df_adj.iloc[0,0][:2]
        month = df_adj.iloc[0,0][-4:] + '-' + df_adj.iloc[0,0][3:5] + '-' + '01'
        generation_kwh = df_adj.iloc[:,1].sum()
        if isinstance(generation_kwh, float):
            compiled: dict = {
                'sgis_name' : [project_name],
                'sgis_tilt' : [project_tilt], 
                'date' : [date_adj], 
                'generation_kwh' : [generation_kwh],
                'month' : month,
                }
            df_final = pd.DataFrame(data=compiled)
            return df_final
        else:
            return None
    except AttributeError:
        return None

def df_compiled(df_unit):
    
    global df_def
    df_def = pd.concat([df_def, df_unit], axis = 0, ignore_index = True)

    return df_def

for file in glob.glob(user + "//Documents//SCPData/*hourly*"):
    output = df_sgis(file)
    df = output[0]
    file_errors = output[1]
    project = name_extract(os.path.split(file)[1])
    project_name: str = project[0]
    project_tilt: str = project[1]
    data_source: str = project[2]
    event = {data_source : file_errors}
    if file_errors:
        errors.update(event)
    else:
        df_compiled(df_unit(df, project_name, project_tilt))
        
path = user + '/Documents/PVSpot/'
df_def.to_csv(path + f"sgis_generation.csv", encoding='utf-8', header = True, sep = ";", index = False)


