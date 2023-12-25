from peewee import *
import settings

db: SqliteDatabase = SqliteDatabase(f'{settings.DATABASE_PATH}{settings.DATABASE_NAME}')


class BaseModel(Model):
    class Meta:
        database = db

class Post(BaseModel):
    title = CharField(max_length=55, default='')

class Department(BaseModel):
    title = CharField(max_length=55, default='')

class Staff(BaseModel):
    FIO = CharField(max_length=55, default='')
    id_post = IntegerField(default=None)
    id_department = IntegerField(default=None)

class Role(BaseModel):
    title = CharField(max_length=55, default='')

class Users(BaseModel):
    FIO = CharField(max_length=55, default='')
    login = CharField(max_length=55, default='')
    password = CharField(max_length=55, default='')
    id_role = IntegerField(default=None)

class Type_of_treatment(BaseModel):
    title = CharField(max_length=55, default='')

class Status_request(BaseModel):
    title = CharField(max_length=55, default='')

class Request(BaseModel):
    add_data = TextField(default='')
    id_status_req = IntegerField(default=None)
    id_user = IntegerField(default=None)

class Type_of_disease(BaseModel):
    title = CharField(max_length=55, default='')

class Disease(BaseModel):
    title = CharField(max_length=55, default='')
    description = CharField(default='')
    id_type_of_disease = IntegerField(default=None)

class Reception(BaseModel):
    id_req = IntegerField(default=None)
    id_staff = IntegerField(default=None)
    id_disease = IntegerField(default=None)
    id_type_of_treatment = IntegerField(default=None)
    description_of_treatment = CharField(default='')

class Treatment_status(BaseModel):
    title = CharField(max_length=55, default='')

class Patients(BaseModel):
    id_reception = IntegerField(default=None)
    id_status = IntegerField(default=None)
    data_of_discharge = TextField(default='')


db.create_tables([
    Post, 
    Department,
    Staff,
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