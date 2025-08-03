import os
import boto3
from supabase import create_client, Client
from typing import List, Dict
from crud import CRUDservice

# Supabase
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
negative_path: str = os.environ.get("NEGATIVE_PATH")
crud_service = CRUDservice(supabase)

# AWS S3
s3 = boto3.client(
    's3',
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY"),
    aws_secret_access_key = os.environ.get("AWS_ACCESS_SECRET_KEY"),
    region_name = os.environ.get("AWS_REGION")
)


def insert_negative_to_sp() -> None:
    try:
        img_urls: List[Dict[str, str]] = insert_negative_to_s3()
        crud_service.add_bulk_negative_images(img_urls)


    except Exception as e:
        return e


def insert_negative_to_s3() -> List[Dict[str, str]]:
    try:
        pass

    except Exception as e:
        return e
