import pandas as pd
from src.utils.logger import logger


def validate_dataframe(df: pd.DataFrame, table_name: str) -> bool:
    """
    Validate the Dataframe before transformation.
    Returns True if validation passes, otherwise False.
    """

    logger.info(f"\n Validating {table_name}...")

    # Check if Dataframe is empty
    if df.empty:
        logger.info("Dataframe is empty.")
        return False
    
    duplicate_count = df.duplicated().sum()

    if duplicate_count  > 0:
        logger.info(f"Duplicate records found: {duplicate_count}")
    else:
        logger.info("No duplicate records found.")
    
    missing_values = df.isnull().sum()

    logger.info("\n Missing values:")
    logger.info("\n%s", missing_values)

    logger.info("\n Validation completed successfully.")

    return True