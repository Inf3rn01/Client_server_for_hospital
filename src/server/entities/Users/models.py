from pydantic import BaseModel
from typing import Optional

def User(BaseModel):
    id: Optional[int]
    FIO: str
    login: str
    password: str