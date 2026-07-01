from io import BytesIO

import pandas as pd

from src.aws.s3_client import get_s3_client
from src.config.settings import S3_BUCKET


def read_csv_from_s3(s3_key: str):

    client = get_s3_client()

    response = client.get_object(
        Bucket=S3_BUCKET,
        Key=s3_key
    )

    return pd.read_csv(
        BytesIO(response["Body"].read())
    )