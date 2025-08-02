from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
    id: str
    time_stamp: datetime
    ttl: int = Field(1, description="Time-to-live in hour")