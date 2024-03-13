import pytest
from datetime import datetime
from app.contract import Files
from datetime import date, time
from pydantic import ValidationError

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

    raw_data = {
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

    file = Files(**raw_data)

    assert file.Date == raw_data['Date']
    assert file.Time == raw_data['Time']
    assert file.GHI == raw_data['GHI']
    assert file.DIF == raw_data['DIF']
    assert file.DNI == raw_data['DNI']
    assert file.GTI == raw_data['GTI']
    assert file.SE == raw_data['SE']
    assert file.SA == raw_data['SA']
    assert file.TEMP == raw_data['TEMP']
    assert file.WS == raw_data['WS']
    assert file.WD == raw_data['WD']
    assert file.PVOUT == raw_data['PVOUT']

def test_invalid_raw_data_format():
    """
    Tests the creation of an instance of the File class with invalid data due to incorrect format.
    """

    raw_data = {
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

    with pytest.raises(ValidationError):
        Files(**raw_data)
    