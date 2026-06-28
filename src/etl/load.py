from psycopg2.extras import execute_batch
import psycopg2
import pandas as pd
from src.utils.logger import logger
from src.config.settings import BATCH_SIZE
from src.exceptions.etl_exceptions import LoadError


PRIMARY_KEYS = {
    "customers": "customer_id",
    "products": "product_id",
    "orders": "order_id",
    "order_items": "order_item_id"
}


def load_dataframe(
        df: pd.DataFrame,
        table_name: str,
        connection
) -> None:
    """
    Generic function to load any dataframe
    into PostgreSQL.
    Raises LoadError if loading fails.
    """

    cursor = None
    try:
        cursor = connection.cursor()

        primary_key = PRIMARY_KEYS.get(table_name)

        if primary_key is None:
            raise LoadError(
                f"No primary key configured for table: {table_name}"
            )

        columns = list(df.columns)

        placeholders = ", ".join(
            ["%s"] * len(columns)
        )

        update_clause = build_update_clause(
            columns,
            primary_key
        )

        columns_str = ", ".join(columns)
        
        query = f"""
            INSERT INTO ecommerce.{table_name}
            ({columns_str})
            VALUES ({placeholders})

            ON CONFLICT ({primary_key})

            DO UPDATE SET

            {update_clause};
        """

        records = list(
            df.itertuples(index=False, name=None)
        )

        execute_batch(
            cursor,
            query,
            records,
            page_size=BATCH_SIZE
        )

        connection.commit()

        logger.info(
            f"✓ {len(records)} rows loaded into {table_name}"
        )

    except psycopg2.Error as e:
        connection.rollback()
        logger.error(f"Database error while loading {table_name}")
        logger.exception(f"Error loading {table_name}")
        raise LoadError(f"Failed to load data into {table_name}") from e

    except LoadError:
        connection.rollback()
        raise

    except Exception as e:
        connection.rollback()
        logger.error(f"❌ Unexpected error while loading {table_name}")
        logger.exception(f"Error loading {table_name}")
        raise LoadError(f"Failed to load data into {table_name}") from e

    finally:
        if cursor:
            cursor.close()


def build_update_clause(columns, primary_key):
    """
    Generate the UPDATE clause dynamically.
    """

    update_columns = [
        column
        for column in columns
        if column != primary_key
    ]

    return ", ".join(
        [
            f"{column}=EXCLUDED.{column}"
            for column in update_columns
        ]
    )