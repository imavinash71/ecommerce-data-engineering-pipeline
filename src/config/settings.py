from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
BASE_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = BASE_DIR / ".env"
load_dotenv(ENV_FILE)

# ===============================
# Project Paths
# ===============================

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


AWS_REGION = os.getenv("AWS_REGION")

S3_BUCKET = os.getenv("S3_BUCKET")

RAW_PREFIX = "raw"

PROCESSED_PREFIX = "processed"

REPORTS_PREFIX = "reports"

LOGS_PREFIX = "logs"

DATA_SOURCE = os.getenv("DATA_SOURCE", "LOCAL")