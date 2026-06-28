from pathlib import Path

# ===============================
# Project Paths
# ===============================

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"

RAW_DATA_PATH = DATA_DIR / "raw"

PROCESSED_DATA_PATH = DATA_DIR / "processed"

LOG_DIR = BASE_DIR / "logs"

SQL_DIR = Path("sql")


# ===============================
# Dataset Configuration
# ===============================

TABLES = [

    ("customers.csv", "customers"),

    ("products.csv", "products"),

    ("orders.csv", "orders"),

    ("order_items.csv", "order_items")

]


# ===============================
# Batch Size
# ===============================

BATCH_SIZE = 100