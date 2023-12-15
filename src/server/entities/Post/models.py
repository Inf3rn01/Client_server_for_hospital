from pydantic import BaseModel

def Post(BaseModel):
    id: optional[int]
    title: str