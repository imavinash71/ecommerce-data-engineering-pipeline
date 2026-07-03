# E-Commerce Data Engineering Pipeline

A production-inspired ETL (Extract, Transform, Load) pipeline built using Python, Pandas, PostgreSQL, Docker, and SQLAlchemy.

The project simulates a real-world e-commerce data pipeline by extracting raw CSV datasets, validating and transforming the data, and loading it into PostgreSQL using an incremental loading strategy (UPSERT).

---

## Features

- Extract data from CSV files
- Validate datasets
  - Duplicate record detection
  - Missing value detection
- Data transformation using Pandas
- Load data into PostgreSQL
- Incremental loading using UPSERT
- Automatic database schema creation
- Centralized configuration using `.env`
- Logging support
- Pipeline execution report generation
- Exception handling
- Unit testing using Pytest
- Docker/Podman support

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.11 |
| Data Processing | Pandas |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Database Driver | psycopg2 |
| Testing | Pytest |
| Configuration | python-dotenv |
| Logging | Python Logging |
| Containerization | Docker / Podman |

---

## Project Structure

```text
ecommerce-data-engineering-pipeline/
│
├── config/
│   └── settings.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│
├── reports/
│
├── sql/
│
├── src/
│   ├── database/
│   ├── etl/
│   ├── generator/
│   ├── pipeline/
│   ├── utils/
│   └── main.py
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ETL Workflow

1. Extract raw CSV files
2. Validate the data
3. Transform the data
4. Save processed files
5. Load into PostgreSQL
6. Generate execution report
7. Write logs

---

## Database Tables

The pipeline loads data into the following PostgreSQL tables:

- customers
- products
- orders
- order_items

---

## Data Validation

The pipeline performs the following validations before loading data:

- Duplicate record detection
- Missing value detection
- Basic data quality checks

---

## Incremental Loading

The pipeline uses PostgreSQL UPSERT (`ON CONFLICT`) to prevent duplicate records.

If a record already exists:

- Existing record is updated

If a record is new:

- New record is inserted

This allows the pipeline to be executed multiple times safely.

---

## Logging

Pipeline execution logs are stored inside:

```text
logs/
```

The logs include:

- Extraction
- Validation
- Transformation
- Loading
- Errors
- Pipeline completion status

---

## Reports

Every pipeline execution generates a summary report containing:

- Total records processed
- Loaded records
- Validation status
- Execution summary

Reports are stored inside:

```text
reports/
```

---

## Unit Testing

Run tests:

```bash
pytest
```

Current tests include:

- Data transformation
- Validation
- Utility functions

---

## Running the Project

### Clone Repository

```bash
git clone <repository-url>
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file.

Example:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ecommerce_db
DB_USER=postgres
DB_PASSWORD=postgres
```

### Run Pipeline

```bash
python -m src.main
```

---

## Sample Output

```text
Processing customers...

Validation completed successfully.

Loaded 100 rows into customers

Processing products...

Loaded 50 rows into products

Processing orders...

Loaded 500 rows into orders

Processing order_items...

Loaded 1200 rows into order_items

ETL Pipeline Completed Successfully.
```

---

## Future Enhancements

- AWS S3 Integration
- Apache Airflow Orchestration
- PySpark Implementation
- CI/CD Pipeline
- Data Warehouse Integration
- Dashboard & Analytics

---

## Author

**Avinash Chavhan**

Data Engineering Portfolio Project