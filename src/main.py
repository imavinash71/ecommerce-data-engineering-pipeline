from src.config.db import get_connection

from src.etl.extract import extract_csv
from src.etl.validate import validate_dataframe
from src.etl.transform import (
    transform_customers,
    save_processed_data
)
from src.etl.load import load_dataframe
from src.utils.logger import logger
from src.config.settings import TABLES
import time
from src.utils.report_generator import PipelineReport
from src.exceptions.etl_exceptions import ETLError



def main():

    connection = get_connection()

    try:

        start_time = time.perf_counter()
        report = PipelineReport()
        
        print("\n Starting ETL Pipeline...\n")
        logger.info("Starting ETL Pipeline...")

        for file_name, table_name in TABLES:

            print(f"\n Processing {table_name}...")
            logger.info(f"Processing {table_name}")

            df = extract_csv(file_name)

            validation = validate_dataframe(df, table_name)

            if not validation["is_valid"]:
                print(f"Validation failed for {table_name}. Skipping...")
                logger.warning(f"Validation failed for {table_name}. Skipping...")
                continue

            print(f"✓ Validation passed: {len(df)} records")

            # Only customers need transformation for now
            if table_name == "customers":
                print(f" Transforming {table_name} data...")
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

            report.add_table(
                table_name=table_name,
                rows_processed=len(df),
                duplicates=validation["duplicates"],
                missing_values=validation["missing_values"],
                rows_loaded=len(df)
            )

        print("\n ETL Pipeline Completed Successfully!")
        logger.info("ETL Pipeline Completed Successfully.")

        duration = time.perf_counter() - start_time

        report_file = report.save(duration)

        print(f" Pipeline report generated: {report_file}")
        logger.info(f"Pipeline report generated: {report_file}")

    finally:

        connection.close()


if __name__ == "__main__":
    
    try:
        main()

    except ETLError as e:
        print(f"\n ETL Error: {e}")
        logger.error(f"ETL Error: {e}")

    except Exception as e:
        print(f"\n Unexpected Error: {e}")
        logger.exception(f"Unexpected Error: {e}")