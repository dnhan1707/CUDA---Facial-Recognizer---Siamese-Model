import os
import boto3
import uuid
from typing import List
from dotenv import load_dotenv

load_dotenv()


class ImageController():
    def __init__(self):
        self.s3_client = boto3.client(
            service_name='s3',
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY"),
            aws_secret_access_key=os.environ.get("AWS_ACCESS_SECRET_KEY"),
            region_name=os.environ.get("AWS_REGION")
        )
        self.AWS_BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME")

    def upload_images(self, files: List, folder: str, user_id: str) -> str:
        try:
            if not user_id:
                user_id = str(uuid.uuid4())
            
            for file in files:
                s3_key = f"{folder}/{user_id}/{file.filename}"
                self.s3_client.upload_fileobj(file.file, self.AWS_BUCKET_NAME, s3_key)

            return user_id
        
        except Exception as e:
            return str(e)  # Optionally, convert exception to string for clearer error
    
    def get_images(self, folder: str, user_id: str):
        try:
            prefix = f"{folder}/{user_id}/"
            response = self.s3_client.list_objects_v2(
                Bucket=self.AWS_BUCKET_NAME,
                Prefix=prefix
            )
            image_urls = []
            for obj in response.get("Contents", []):
                key = obj["Key"]
                url = f"https://{self.AWS_BUCKET_NAME}.s3.amazonaws.com/{key}"
                image_urls.append(url)
            return image_urls

        except Exception as e:
            return e


