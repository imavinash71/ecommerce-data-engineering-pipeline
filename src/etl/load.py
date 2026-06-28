from psycopg2.extras import execute_batch
import pandas as pd


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
    """

    cursor = connection.cursor()

    primary_key = PRIMARY_KEYS.get(table_name)

    if primary_key is None:
        raise ValueError(
            f"No primary key configured for table: {table_name}"
        )

    columns = ", ".join(df.columns)

    placeholders = ", ".join(
        ["%s"] * len(df.columns)
    )

    query = f"""
        INSERT INTO ecommerce.{table_name}
        ({columns})
        VALUES ({placeholders})
        ON CONFLICT ({primary_key})
        DO NOTHING;
    """

    records = list(
        df.itertuples(index=False, name=None)
    )

    try:

        execute_batch(
            cursor,
            query,
            records,
            page_size=100
        )

        connection.commit()

        print(
            f"✅ Loaded {len(records)} rows into {table_name}"
        )

    except Exception as e:

        connection.rollback()

        print(
            f"❌ Error while loading {table_name}"
        )

        print(e)

        raise

    finally:

        cursor.close()