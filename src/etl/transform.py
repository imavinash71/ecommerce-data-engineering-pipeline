from pathlib import Path
import pandas as pd
from src.config.settings import PROCESSED_DATA_PATH
from src.utils.logger import logger
from src.exceptions.etl_exceptions import TransformError


def transform_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform customer data and return a cleaned Dataframe.
    Raises TransformError if transformation fails.
    """
    try:
        logger.info("Transforming customer data...")
        
        # Remove duplicate rows
        df = df.drop_duplicates()

        df["registration_date"] = pd.to_datetime(
            df["registration_date"],
            errors='coerce'
        )

        text_columns = [
            "first_name",
            "last_name",
            "email",
            "city",
            "state",
            "country"
        ]

        for column in text_columns:
            if column in df.columns:
                df[column] = df[column].str.strip()

        # Convert phone number to string
        if "phone" in df.columns:
            df["phone"] = df["phone"].astype(str)

        logger.info("Customer transformation completed successfully.")
        return df
    
    except Exception as e:
        logger.exception("Customer transformation failed")
        raise TransformError("Failed to transform customer data") from e


def save_processed_data(df: pd.DataFrame, file_name: str) -> Path:
    """
    Save processed data to CSV file.
    Returns the output path.
    Raises TransformError if save fails.
    """
    try:
        output_path = PROCESSED_DATA_PATH / file_name
        
        PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

        df.to_csv(output_path, index=False)

        logger.info(f"Processed file saved to: {output_path}")
        
        return output_path
    
    except IOError as e:
        logger.error(f"Failed to save file {file_name}")
        raise TransformError(f"Failed to save processed data to {file_name}") from e
    
    except Exception as e:
        logger.exception(f"Error saving processed data {file_name}")
        raise TransformError(f"Failed to save processed data to {file_name}") from e