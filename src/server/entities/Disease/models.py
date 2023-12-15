from pydantic import BaseModel

def Disease(BaseModel):
    id: optional[int]
    title: str
    descriptional: optional[str]
    id_type_of_disease: int