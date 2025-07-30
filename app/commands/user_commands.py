from datetime import datetime
from pydantic import BaseModel


class CreateUserCommand(BaseModel):
    name: str
    email: str
    created_at: datetime = datetime.now()
