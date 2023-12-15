from pydantic import BaseModel

def Role(BaseModel):
    id: optional[int]
    title: str