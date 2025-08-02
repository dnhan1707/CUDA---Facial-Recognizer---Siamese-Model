from fastapi import FastAPI
from app.schema.user import User


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
    async def upload_image(user: User):
        pass

    @app.post("/train")
    async def train_model(user: User):
        pass
    

    @app.post("/predict")
    async def predict(user: User):
        pass

    return app

app = create_application()
