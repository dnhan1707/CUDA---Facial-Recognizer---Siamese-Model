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
                s3_key = f"{folder}/{user_id}/{file.file_name}"
                self.s3_client.upload_fileobj(file.file, self.AWS_BUCKET_NAME, s3_key)

            return user_id
        
        except Exception as e:
            return e
        
    
    def get_images():
        pass


