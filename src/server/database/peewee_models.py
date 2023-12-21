import peewee
from peewee import *
from settings import DB_PATH

db = peewee.SqliteDatabase(database=DB_PATH)


class BaseModel(Model):
    class Meta:
        database = db


class Posts(BaseModel):
    title: CharField()


class Departments(BaseModel):
    title: CharField()


class Staff(BaseModel):
    FIO: CharField()
    id_post: ForeignKeyField(Posts, on_delete="CASCADE", default=0)
    id_department: ForeignKeyField(Departments, on_delete="CASCADE", default=0)


class Roles(BaseModel):
    title: CharField()


class Users(BaseModel):
    FIO: CharField()
    login: CharField()
    password: CharField()
    id_role: ForeignKeyField(Roles, on_delete="CASCADE", default=0)


class Type_of_treatments(BaseModel):
    title: CharField()


class Status_requests(BaseModel):
    title: CharField()


class Requests(BaseModel):
    add_data: DateField()
    id_status_req: ForeignKeyField(Status_requests, on_delete="CASCADE", default=0)
    id_user: ForeignKeyField(Users, on_delete="CASCADE", default=0)


class Type_of_diseases(BaseModel):
    title: CharField()


class Diseases(BaseModel):
    title: CharField()
    description: CharField()
    id_type_of_disease: ForeignKeyField(Type_of_diseases, on_delete="CASCADE", default=0)


class Receptions(BaseModel):
    id_req: ForeignKeyField(Requests, on_delete="CASCADE", default=0)
    id_staff: ForeignKeyField(Staff, on_delete="CASCADE", default=0)
    id_disease: ForeignKeyField(Diseases, on_delete="CASCADE", default=0)
    id_type_of_treatment: ForeignKeyField(Type_of_treatments, on_delete="CASCADE", default=0)
    description_of_treatment: CharField()


class Treatment_status(BaseModel):
    title: CharField()


class Patients(BaseModel):
    id_reception: ForeignKeyField(Receptions, on_delete="CASCADE", default=0)
    id_status: ForeignKeyField(Treatment_status, on_delete="CASCADE", default=0)
    data_of_discharge: DateField()


with db:
    db.create_tables([
        Posts,
        Departments,
        Staff,
        Roles,
        Users,
        Type_of_treatments,
        Status_requests,
        Requests,
        Type_of_diseases,
        Diseases,
        Receptions,
        Treatment_status,
        Patients
    ])

print("Done")
