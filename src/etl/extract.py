from pathlib import Path
import pandas as pd
from src.utils.logger import logger
from src.config.settings import RAW_DATA_PATH
from src.exceptions.etl_exceptions import ExtractError
from src.config.settings import DATA_SOURCE
from src.aws.s3_download import read_csv_from_s3


def extract_csv(local_path: str, s3_key: str = None):
    """
    Read a CSV file from the raw data folder
    and return it as Pandas Dataframe.
    """
    try:
        if DATA_SOURCE.upper() == "LOCAL":

            logger.info(f"Reading local file: {local_path}")

            return pd.read_csv(local_path)

        elif DATA_SOURCE.upper() == "S3":

            logger.info(f"Reading S3 file: {s3_key}")

            return read_csv_from_s3(s3_key)

        else:
            raise ValueError(f"Unsupported DATA_SOURCE: {DATA_SOURCE}")
    
    except FileNotFoundError as e:
        logger.error(f"File not found: {local_path}")
        raise ExtractError(f"Failed to extract {local_path}: File not found") from e
    
    except pd.errors.ParserError as e:
        logger.error(f"CSV parsing error in {local_path}")
        raise ExtractError(f"Failed to parse CSV file {local_path}") from e
    
    except Exception as e:
        logger.exception(f"Extraction failed for {local_path}")
        raise ExtractError(f"Failed to extract {local_path}") from e
