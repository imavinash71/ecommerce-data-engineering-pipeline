from src.aws.s3_client import get_s3_client
from src.config.settings import S3_BUCKET


def list_objects(prefix=""):

    client = get_s3_client()

    response = client.list_objects_v2(
        Bucket=S3_BUCKET,
        Prefix=prefix
    )

    if "Contents" not in response:
        print("No files found.")
        return

    print("\nObjects in S3:\n")

    for obj in response["Contents"]:
        print(obj["Key"])