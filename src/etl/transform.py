from pathlib import Path
import pandas as pd
from src.config.settings import PROCESSED_DATA_PATH


def transform_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform customer data and return a cleaned Dataframe.
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    df["registration_date"] = pd.to_datetime(
        df["registration_date"]
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
        df[column] = df[column].str.strip()

        # Convert phone number to string
        df["phone"] = df["phone"].astype(str)

        return df

def save_processed_data(df: pd.DataFrame, file_name: str):

    output_path = PROCESSED_DATA_PATH / file_name

    df.to_csv(output_path, index=False)

    print(f"Processed file saved to: {output_path}")