from peewee import *
import settings

db = SqliteDatabase(f'{settings.DATABASE_PATH}')


class BaseModel(Model):
    class Meta:
        database = db


class Post(BaseModel):
    title = CharField(default='')


class Department(BaseModel):
    title = CharField(default='')


class Role(BaseModel):
    title = CharField(default='')


class Users(BaseModel):
    FIO = CharField(default='')
    id_role = IntegerField(default=None)


class AuthData(BaseModel):
    login = CharField(default="")
    password = CharField(default="")
    id_user = ForeignKeyField(Users, related_name='auth_data_user_id', default=0)


class Staff(BaseModel):
    id_user = ForeignKeyField(Users, default=2)
    id_post = ForeignKeyField(Post, default=None)
    id_department = ForeignKeyField(Department, default=None)


class Type_of_treatment(BaseModel):
    title = CharField(default='')


class Status_request(BaseModel):
    title = CharField(default='')


class Request(BaseModel):
    add_data = DateField(default='')
    id_status_req = ForeignKeyField(Status_request, default=2)
    id_user = ForeignKeyField(Users, default=1)


class Type_of_disease(BaseModel):
    title = CharField(default='')


class Disease(BaseModel):
    title = CharField(default='')
    description = CharField(default='')
    id_type_of_disease = ForeignKeyField(Type_of_disease, default=0)


class Reception(BaseModel):
    id_req = ForeignKeyField(Request, default=None)
    id_staff = ForeignKeyField(Staff, default=None)
    id_disease = ForeignKeyField(Disease, default=None)
    id_type_of_treatment = ForeignKeyField(Type_of_treatment, default=None)
    description_of_treatment = CharField(default='')


class Treatment_status(BaseModel):
    title = CharField(default='')


class Patients(BaseModel):
    id_reception = ForeignKeyField(Reception, default=None)
    id_status = ForeignKeyField(Treatment_status, default=None)
    data_of_discharge = DateField()


db.create_tables([
    Post, 
    Department,
    Staff,
    AuthData,
    Role,
    Users,
    Type_of_disease,
    Type_of_treatment,
    Request,
    Status_request,
    Disease,
    Reception,
    Treatment_status,
    Patients
])
