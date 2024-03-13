import pytest
from datetime import datetime
from app.contract import Files
from datetime import date, time

def test_valid_raw_data():
    """
    Tests the creation of an instance of the File class with valid data.

    Checks if the File class accepts and stores the valid data correctly. Valid data includes:
    1. First column should be a ISO date (YYYY-MM-DD)
    2. Second column should be of timestamp type (hh:mm)
    3. Third to sixth columns should be positive integers
    4. Seventh and eighth columns should be float
    5. Ninth column should be positive float 
    6. Tenth column should be positive integer
    7. Eleventh column should be positive float with three decimals 
    """

    valid_raw_data = {
        "Date": datetime.now().date(),
        "Time": datetime.now().time(),
        "GHI" : 5,
        "DIF" : 34,
        "DNI" : 298,
        "GTI" : 901,
        "SE"  : -231.42,
        "SA"  : -11.02,
        "TEMP": 20.2,
        "WS"  : 2.11,
        "WD"  : 120,
        "PVOUT": 12.244, 
    }

    file = Files(**valid_raw_data)

    assert file.Date == valid_raw_data['Date']
    assert file.Time == valid_raw_data['Time']
    assert file.GHI == valid_raw_data['GHI']
    assert file.DIF == valid_raw_data['DIF']
    assert file.DNI == valid_raw_data['DNI']
    assert file.GTI == valid_raw_data['GTI']
    assert file.SE == valid_raw_data['SE']
    assert file.SA == valid_raw_data['SA']
    assert file.TEMP == valid_raw_data['TEMP']
    assert file.WS == valid_raw_data['WS']
    assert file.WD == valid_raw_data['WD']
    assert file.PVOUT == valid_raw_data['PVOUT']

def test_invalid_raw_data_format():
    """
    Tests the creation of an instance of the File class with invalid data due to incorrect format.
    """

    invalid_raw_data = {
        "Date": "2012-13-02",
        "Time": "25:41",
        "GHI" : 5.1,
        "DIF" : -34,
        "DNI" : 298,
        "GTI" : "901",
        "SE"  : -231.42,
        "SA"  : -11.02,
        "TEMP": 20.2,
        "WS"  : 2.11,
        "WD"  : 120.01,
        "PVOUT": "-12.4g", 
    }

    file = Files(**invalid_raw_data)

    assert file.Date == invalid_raw_data['Date']
    assert file.Time == invalid_raw_data['Time']
    assert file.GHI == invalid_raw_data['GHI']
    assert file.DIF == invalid_raw_data['DIF']
    assert file.DNI == invalid_raw_data['DNI']
    assert file.GTI == invalid_raw_data['GTI']
    assert file.SE == invalid_raw_data['SE']
    assert file.SA == invalid_raw_data['SA']
    assert file.TEMP == invalid_raw_data['TEMP']
    assert file.WS == invalid_raw_data['WS']
    assert file.WD == invalid_raw_data['WD']
    assert file.PVOUT == invalid_raw_data['PVOUT']