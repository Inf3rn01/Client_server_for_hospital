from pydantic import BaseModel

def Staff(BaseModel):
    id: optional[int]
    FIO: str
    id_post: int
    id_department: int