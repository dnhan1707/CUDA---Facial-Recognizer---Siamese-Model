from fastapi import FastAPI, UploadFile, File
from app.schema.user import User
from typing import List, Literal
from app.controller.image_controller import ImageController

image_controller = ImageController()

def create_application() -> FastAPI:
    app = FastAPI(
        title="Siamese Model API"
    )
    
    @app.get("/")
    async def health_check():
        return {
            "message": "API is running"
        }

    @app.post("/upload")
    async def upload_image(
        folder: Literal["anchor", "positive"],
        user_id: str = "",
        files: List[UploadFile] = File(...)
    ):
        try:
            return image_controller.upload_images(files, folder, user_id)
        except Exception as e:
            return e


    @app.post("/train")
    async def train_model(user: User):
        pass
    

    @app.post("/predict")
    async def predict(user: User):
        pass

    return app

app = create_application()
