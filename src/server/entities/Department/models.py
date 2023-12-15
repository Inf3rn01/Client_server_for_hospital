from pydantic import BaseModel

def Department(BaseModel):
    id: optional[int]
    title: str
