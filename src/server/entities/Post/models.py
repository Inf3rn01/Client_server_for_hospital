from pydantic import BaseModel
from typing import Optional

def Post(BaseModel):
    id: Optional[int]
    title: str