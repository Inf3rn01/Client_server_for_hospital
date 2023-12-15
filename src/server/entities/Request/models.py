from pydantic import BaseModel
from typing import Optional
def Request(BaseModel):
    id: Optional[int]
    add_data: str
    id_status_req: int
    id_user: int