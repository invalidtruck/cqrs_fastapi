from pydantic import BaseModel
from typing import Optional

class GetUserByIdQuery(BaseModel):
    user_id: Optional[str] = None