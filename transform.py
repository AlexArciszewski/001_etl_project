import pandas as pd



def data_transform(df: pd.DataFrame) -> pd.DataFrame:
    """Transforms raw data into clean data

    Args:
        df (pd.DataFrame): raw data from extract.py

    Returns:
        df = pd.DataFrame: cleared data
    """
    
    print(f"\nDataFrame shape: {df.shape}")
    print("\nFirst 2 rows:")
    print(df.head(2))
    
    df = df.copy()
    df = df.dropna()
    df =df.drop_duplicates()
    print(df.shape)    
    return df


