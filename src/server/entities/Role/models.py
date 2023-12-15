from pydantic import BaseModel
from typing import Optional

def Role(BaseModel):
    id: Optional[int]
    title: str