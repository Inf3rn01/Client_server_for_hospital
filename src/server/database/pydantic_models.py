from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = 1


class User(BaseModelModify):
    fullname: str
    balance: float
    regular: bool


class AuthData(BaseModelModify):
    login: str
    password: Optional[str]
    user_id: int


class Staff(BaseModelModify):
    power_level: int = 1
    user_id: int


class Product(BaseModelModify):
    name: str
    price: float


class UserOrder(BaseModelModify):
    count: int
    user_id: int
    product_id: int


class Discount(BaseModelModify):
    product_id: int
    percent: float
    active: bool


class Storage(BaseModelModify):
    address: str


class UserDiscount(BaseModelModify):
    user_id: int
    product_id: int
    percent: float


class StorageOrder(BaseModelModify):
    product_id: int
    storage_id: int
    count: int


class ProductInStorage(BaseModelModify):
    product_id: int
    storage_id: int
    count: int


class LoginData(BaseModel):
    login: str
    password: str
