from pydantic import BaseModel
from typing import Optional

class DefaultResponses(BaseModel):
    msg: str
    id: Optional[int] = None
