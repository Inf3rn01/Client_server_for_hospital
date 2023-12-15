from pydantic import BaseModel
from typing import Optional
def Reception(BaseModel):
    id: Optional[int]
    id_req: int
    id_staff: int
    id_disease: int
    id_type_of_treatment: int
    description_of_treatment: str