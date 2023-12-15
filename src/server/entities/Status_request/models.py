from pydantic import BaseModel

def Status_Request(BaseModel):
    id: optional[int]
    title: str