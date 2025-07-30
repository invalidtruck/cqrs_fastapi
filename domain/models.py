from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id: str
    name: str
    email: str
    created_at: datetime = Field(default_factory=datetime.now)
    


class UserCreatedEvent(BaseModel):
    user_id: str
    name: str
    email: str 
    timestamp: datetime = datetime.now()
    event_type: str = "UserCreated"


