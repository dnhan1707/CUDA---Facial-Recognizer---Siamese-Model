import os
from dotenv import load_dotenv
import boto3
from typing import List, Dict

load_dotenv()

negative_path: str = os.environ.get("NEGATIVE_PATH")

# AWS S3
s3_client = boto3.client(
    service_name='s3',
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("AWS_ACCESS_SECRET_KEY"),
    region_name=os.environ.get("AWS_REGION")
)
AWS_BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME")


def insert_negative_to_sp() -> None:
    try:
        img_urls: List[Dict[str, str]] = insert_negative_to_s3()
    except Exception as e:
        return e


def insert_negative_to_s3() -> List[Dict[str, str]]:
    try:
        files = os.listdir(negative_path)

        for file_name in files:
            full_path = os.path.join(negative_path, file_name)
            s3_key = f"negative/{file_name}"  
            s3_client.upload_file(full_path, AWS_BUCKET_NAME, s3_key)

    except Exception as e:
        return e

def main():
    result = insert_negative_to_sp()
    if result is not None:
        print("Error:", result)
    else:
        print("Negative images upload and inserted successfully")

if __name__ == "__main__":
    main()