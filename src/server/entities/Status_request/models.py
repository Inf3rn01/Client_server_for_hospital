from pydantic import BaseModel
from typing import Optional

def Status_Request(BaseModel):
    id: Optional[int]
    title: str