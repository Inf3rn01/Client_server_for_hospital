from pydantic import BaseModel
from typing import Optional
def Disease(BaseModel):
    id: Optional[int]
    title: str
    descriptional: optional[str]
    id_type_of_disease: int