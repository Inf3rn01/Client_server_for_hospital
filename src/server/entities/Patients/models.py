from pydantic import BaseModel
from typing import Optional

def Patient(BaseModel):
    id: Optional[int]
    id_reception: int
    id_status: int
    data_of_discharge: str