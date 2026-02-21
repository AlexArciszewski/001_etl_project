import pandas as pd
from pathlib import Path
#pytest nazwa_pliku.py -v
from load import save_data


def test_save_data_csv() -> None:
    
    df = pd.DataFrame({
        "name" : ["Alex", "John"],
        "age" : [30,25]
    })
    
    path = Path("tests/test_output.csv")
    
    result = save_data(df, path)
    
    assert result is True
    assert path.exists()
    
    path.unlink()

    
def test_save_xlsx() -> None:
    
    df = pd.DataFrame({
        "name" : ["Alex", "John"],
        "age" : [30,25]
    })  
    
    path = Path("tests/test_output.xlsx")
    
    result = save_data(df, path)
    
    assert result is True
    assert path.exists()
    
    path.unlink()


def test_save_json() -> None:
    
    df = pd.DataFrame({
        "name" : ["Alex", "John"],
        "age" : [30,25]
    }) 
    
    path = Path("tests/test_output.json")
    
    result = save_data(df, path)
    
    assert result is True
    assert path.exists()
    
    path.unlink()
    
    
def test_save_data_invalid_extension() -> None:
    
    path = Path("tests/test_output.txt")
    
    df = pd.DataFrame({
        "name" : ["Alex", "John"],
        "age" : [30,25]
    }) 
    
    result = save_data(df, path)
    
    assert result is False
    assert not path.exists()
    
    