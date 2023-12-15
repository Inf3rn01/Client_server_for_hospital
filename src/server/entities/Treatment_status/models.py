from pydantic import BaseModel
from typing import Optional

def Treatment_status(BaseModel):
    id: Optional[int]
    title: str
