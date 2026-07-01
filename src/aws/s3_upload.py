from pathlib import Path

from src.aws.s3_client import get_s3_client
from src.config.settings import (
    S3_BUCKET,
    RAW_PREFIX
)

from src.utils.logger import logger


def upload_file(local_file_path: str, s3_key: str):
    """
    Upload a single file to S3.
    """

    client = get_s3_client()

    client.upload_file(
        Filename=local_file_path,
        Bucket=S3_BUCKET,
        Key=s3_key
    )

    logger.info(f"Uploaded {local_file_path} -> s3://{S3_BUCKET}/{s3_key}")

from datetime import datetime


def upload_directory(local_directory: str):

    today = datetime.today()

    date_path = today.strftime("%Y/%m/%d")

    directory = Path(local_directory)

    for file in directory.glob("*.csv"):

        s3_key = f"{RAW_PREFIX}/{date_path}/{file.name}"

        upload_file(
            str(file),
            s3_key
        )