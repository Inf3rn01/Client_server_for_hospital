from pydantic import BaseModel

def Request(BaseModel):
    id: optional[int]
    add_data: str
    id_status_req: int
    id_user: int