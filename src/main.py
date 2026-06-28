from config.db import get_connection

from src.etl.extract import extract_csv
from src.etl.validate import validate_dataframe
from src.etl.transform import (
    transform_customers,
    save_processed_data
)
from src.etl.load import load_dataframe


TABLES = [

    ("customers.csv", "customers"),

    ("products.csv", "products"),

    ("orders.csv", "orders"),

    ("order_items.csv", "order_items")

]


def main():

    connection = get_connection()

    try:

        for file_name, table_name in TABLES:

            print(f"\nProcessing {table_name}...")

            df = extract_csv(file_name)

            if not validate_dataframe(df, table_name):
                continue

            # Only customers need transformation for now
            if table_name == "customers":
                df = transform_customers(df)

            save_processed_data(
                df,
                file_name
            )

            load_dataframe(
                df,
                table_name,
                connection
            )

        print("\n🎉 ETL Pipeline Completed Successfully!")

    finally:

        connection.close()


if __name__ == "__main__":
    main()