from pathlib import Path
import pandas as pd
from src.utils.logger import logger
from src.config.settings import RAW_DATA_PATH



def extract_csv(file_name: str)-> pd.DataFrame:
    """
    Read a CSV file from the raw data folder
    and return it as Pandas Dataframe.
    """

    file_path = RAW_DATA_PATH/file_name

    logger.info(f"Extracting {file_name}")

    df = pd.read_csv(file_path)

    logger.info(
    f"{len(df)} records extracted from {file_name}"
)
    
    return df
