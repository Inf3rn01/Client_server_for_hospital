from pydantic import BaseModel
from typing import Optional
def Department(BaseModel):
    id: Optional[int]
    title: str
