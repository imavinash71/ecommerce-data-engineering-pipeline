from pathlib import Path
import pandas as pd
from src.utils.logger import logger
from src.config.settings import RAW_DATA_PATH
from src.exceptions.etl_exceptions import ExtractError


def extract_csv(file_name: str) -> pd.DataFrame:
    """
    Read a CSV file from the raw data folder
    and return it as Pandas Dataframe.
    """
    try:
        file_path = RAW_DATA_PATH / file_name
        
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        logger.info(f"Extracting {file_name}")

        df = pd.read_csv(file_path)
        
        if df.empty:
            raise ExtractError(f"Extracted file {file_name} is empty")

        logger.info(f"{len(df)} records extracted from {file_name}")
    
        return df
    
    except FileNotFoundError as e:
        logger.error(f"File not found: {file_name}")
        raise ExtractError(f"Failed to extract {file_name}: File not found") from e
    
    except pd.errors.ParserError as e:
        logger.error(f"CSV parsing error in {file_name}")
        raise ExtractError(f"Failed to parse CSV file {file_name}") from e
    
    except Exception as e:
        logger.exception(f"Extraction failed for {file_name}")
        raise ExtractError(f"Failed to extract {file_name}") from e
