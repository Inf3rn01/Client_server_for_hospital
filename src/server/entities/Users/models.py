from pydantic import BaseModel


def User(BaseModel):
    id: optional[int]
    FIO: str
    login: str
    password: str