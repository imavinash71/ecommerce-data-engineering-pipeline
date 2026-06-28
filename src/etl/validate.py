import pandas as pd
from src.utils.logger import logger
from src.exceptions.etl_exceptions import ValidationError


def validate_dataframe(df: pd.DataFrame, table_name: str) -> dict:
    """
    Validate the Dataframe before transformation.
    Returns a dictionary with validation status and details.
    Raises ValidationError if validation fails.
    """
    
    try:
        logger.info(f"\nValidating {table_name}...")

        # Check if Dataframe is empty
        if df.empty:
            logger.error(f"Dataframe for {table_name} is empty")
            raise ValidationError(f"Dataframe for {table_name} is empty")
        
        duplicate_count = df.duplicated().sum()

        if duplicate_count > 0:
            logger.warning(f"Duplicate records found: {duplicate_count}")
        else:
            logger.info("No duplicate records found.")
        
        missing_values = df.isnull().sum()
        total_missing = int(missing_values.sum())

        logger.info("\nMissing values:")
        logger.info("\n%s", missing_values)

        logger.info(f"\nValidation completed successfully for {table_name}.")

        return {
            "is_valid": True,
            "duplicates": int(duplicate_count),
            "missing_values": total_missing
        }
    
    except ValidationError:
        raise
    
    except Exception as e:
        logger.exception(f"Validation error for {table_name}")
        raise ValidationError(f"Failed to validate {table_name}") from e