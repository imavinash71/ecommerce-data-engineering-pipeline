from src.aws.s3_client import get_s3_client


def test_connection():

    client = get_s3_client()

    buckets = client.list_buckets()

    print("\nAvailable Buckets:\n")

    for bucket in buckets["Buckets"]:
        print(bucket["Name"])


if __name__ == "__main__":
    test_connection()