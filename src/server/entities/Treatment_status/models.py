from pydantic import BaseModel


def Treatment_status(BaseModel):
    id: optional[int]
    title: str
