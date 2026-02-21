import pandas as pd
from pathlib import Path
#pytest nazwa_pliku.py -v
from load import save_data
import pytest


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "name": ["Alex", "John"],
        "age": [30, 25]
    })



def test_save_data_csv(sample_df) -> None:
    
    
    path = Path("tests/test_output.csv")
    
    result = save_data(sample_df, path)
    
    assert result is True
    assert path.exists()
    
    path.unlink()

    
def test_save_xlsx(sample_df) -> None:
    
    path = Path("tests/test_output.xlsx")
    
    result = save_data(sample_df, path)
    
    assert result is True
    assert path.exists()
    
    path.unlink()


def test_save_json(sample_df) -> None:
    
    path = Path("tests/test_output.json")
    
    result = save_data(sample_df, path)
    
    assert result is True
    assert path.exists()
    
    path.unlink()
    
    
def test_save_data_invalid_extension(sample_df) -> None:
    
    path = Path("tests/test_output.txt")
    
    result = save_data(sample_df, path)
    
    assert result is False
    assert not path.exists()
    
    