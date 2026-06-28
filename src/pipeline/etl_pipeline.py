import time

from src.config.db import get_connection
from src.config.settings import TABLES

from src.etl.extract import extract_csv
from src.etl.validate import validate_dataframe
from src.etl.transform import (
    transform_customers,
    save_processed_data
)
from src.etl.load import load_dataframe

from src.utils.logger import logger
from src.utils.report_generator import PipelineReport


class ETLPipeline:

    def __init__(self):
        self.connection = None
        self.report = PipelineReport()

    def connect(self):
        logger.info("Connecting to PostgreSQL...")
        self.connection = get_connection()

    def close(self):
        if self.connection:
            self.connection.close()
            logger.info("Database connection closed.")

    def process_table(self, file_name, table_name):

        logger.info(f"Processing {table_name}")

        df = extract_csv(file_name)

        validation = validate_dataframe(df, table_name)

        if not validation["is_valid"]:
            logger.warning(f"Validation failed for {table_name}")
            return

        if table_name == "customers":
            df = transform_customers(df)

        save_processed_data(df, file_name)

        load_dataframe(
            df,
            table_name,
            self.connection
        )

        self.report.add_table(
            table_name=table_name,
            rows_processed=len(df),
            duplicates=validation["duplicates"],
            missing_values=validation["missing_values"],
            rows_loaded=len(df)
        )

    def run(self):

        start_time = time.perf_counter()

        try:

            self.connect()

            for file_name, table_name in TABLES:

                self.process_table(
                    file_name,
                    table_name
                )

            duration = time.perf_counter() - start_time

            report_file = self.report.save(duration)

            logger.info(
                f"Pipeline report generated: {report_file}"
            )

            logger.info(
                "ETL Pipeline Completed Successfully."
            )

        finally:

            self.close()