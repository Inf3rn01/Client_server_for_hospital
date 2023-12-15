from pydantic import BaseModel


def Patient(BaseModel):
    id: optional[int]
    id_reception: int
    id_status: int
    data_of_discharge: str