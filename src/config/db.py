import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()


DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}
required = [
    "DB_HOST",
    "DB_PORT",
    "DB_NAME",
    "DB_USER",
    "DB_PASSWORD",
]


for variable in required:
    if not os.getenv(variable):
        raise ValueError(
            f"Missing environment variable: {variable}"
        )

def get_connection():

    return psycopg2.connect(**DB_CONFIG)