import psycopg2


DB_CONFIG = {
    "host": "localhost",
    "port": 5433,
    "database": "ecommerce_db",
    "user": "doc_aiq_admin",
    "password": "docaiqadmin2025"
}


def get_connection():

    connection = psycopg2.connect(**DB_CONFIG)

    return connection