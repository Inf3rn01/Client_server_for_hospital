from pydantic import BaseModel
from typing import Optional

def Staff(BaseModel):
    id: Optional[int]
    FIO: str
    id_post: int
    id_department: int