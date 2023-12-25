from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = 1


class Post(BaseModelModify):
    title: str = ''


class Department(BaseModelModify):
    title: str = ''


class Staff(BaseModelModify):
    id_post: int = None
    id_department: int = None


class Role(BaseModelModify):
    title: str = ''


class Users(BaseModelModify):
    FIO: str = ''
    login: str = ''
    password: str = ''
    id_role: int = None


class Type_of_treatment(BaseModelModify):
    title: str = ''


class Status_request(BaseModelModify):
    title: str = ''


class Request(BaseModelModify):
    add_data: str = ''
    id_status_req: int = None
    id_user: int = None


class Type_of_disease(BaseModelModify):
    title: str = ''


class Disease(BaseModelModify):
    title: str = ''
    description: str = ''
    id_type_of_disease: int = None


class Reception(BaseModelModify):
    id_req: int = None
    id_staff: int = None
    id_disease: int = None
    id_type_of_treatment: int = None
    description_of_treatment: str = ''


class Treatment_status(BaseModelModify):
    title: str = ''


class Patients(BaseModelModify):
    id_reception: int = None
    id_status: int = None
    data_of_discharge: str = ''


class LoginData(BaseModelModify):
    login: str
    password: str


class AuthData(BaseModelModify):
    login: str
    password: str
    user_id: int
