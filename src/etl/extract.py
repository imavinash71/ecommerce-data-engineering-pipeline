from pathlib import Path
import pandas as pd

RAW_DATA_PATH = Path("data/raw")

def extract_csv(file_name: str)-> pd.DataFrame:
    """
    Read a CSV file from the raw data folder
    and return it as Pandas Dataframe.
    """

    file_path = RAW_DATA_PATH/file_name

    df = pd.read_csv(file_path)
    return df
