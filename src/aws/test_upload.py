from src.aws.s3_upload import upload_directory


if __name__ == "__main__":

    upload_directory(
        "data/raw"
    )