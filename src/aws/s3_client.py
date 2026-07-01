import boto3
import os
from src.utils.logger import logger


def get_s3_client():
    """
    Create and return an AWS S3 client using credentials from environment variables.
    """
    
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_region = os.getenv("AWS_REGION", "us-east-1")
    
    if not aws_access_key_id or not aws_secret_access_key:
        logger.warning("AWS credentials not found in environment variables")
    
    try:
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region
        )
        logger.info(f"S3 client created successfully for region: {aws_region}")
        return s3_client
    
    except Exception as e:
        logger.error(f"Failed to create S3 client: {str(e)}")
        raise