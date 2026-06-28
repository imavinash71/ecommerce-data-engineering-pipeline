from pathlib import Path

from src.config.db import get_connection
from src.utils.logger import logger
from src.config.settings import SQL_DIR



def execute_sql_file(cursor, sql_file: Path):

    logger.info(
    f"Running migration: {sql_file.name}"
)

    with open(sql_file, "r", encoding="utf-8") as file:

        lines = file.readlines()
        
        # Remove comments and empty lines
        sql_lines = []
        for line in lines:
            # Remove SQL comments
            if '--' in line:
                line = line[:line.index('--')]
            # Strip whitespace
            line = line.strip()
            if line:
                sql_lines.append(line)
        
        sql_content = " ".join(sql_lines)
        
        # Skip if no actual SQL statements
        if not sql_content or sql_content.isspace():
            logger.warning(f"Skipping empty/comment-only file: {sql_file.name}")
            return

        cursor.execute(sql_content)


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    try:

        sql_files = sorted(SQL_DIR.glob("*.sql"))

        if not sql_files:
            raise FileNotFoundError(
                "No SQL files found."
            )

        for sql_file in sql_files:

            execute_sql_file(
                cursor,
                sql_file
            )

        connection.commit()

        logger.info(
            "Database initialized successfully."
        )

    except Exception:

        connection.rollback()

        logger.exception(
            "Database initialization failed."
        )

        raise

    finally:

        cursor.close()

        connection.close()


if __name__ == "__main__":

    initialize_database()