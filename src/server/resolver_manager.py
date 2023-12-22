import fastapi
import peewee
from typing import Type
from src.server.database.peewee_models import BaseModel
from src.server.database.pydantic_models import ModifyBaseModel


class ResolverManager:

    def __init__(self, peewee_model: Type[BaseModel], pydantic_model:Type[ModifyBaseModel],) -> None:
        self.peewee_model = peewee_model
        self.pydantic_model = pydantic_model

    def check_for_errors(self) -> dict:
        try:
            self.check()
            return {'code': 200, 'msg': 'Successfully', 'result': False}
        except peewee.DatabaseError as error:
            return {'code': 400, 'msg': {error}, 'result': True}
        except peewee.InterfaceError as error:
            return {'code': 400, 'msg': {error}, 'result': True}
        except peewee.DoesNotExist as error:
            return {'code': 201, 'msg': 'There is no existing record to check', 'result': False}


    def check(self, id: int = -1):
        return self.peewee_model.get(self.peewee_model.id == id)


    def new(self, new_model: Type[ModifyBaseModel])->dict:
        if self.check_for_errors()['result']:
            return self.check_for_errors()

        new_peewee_model = self.peewee_model.create()

        for atr in dir(new_model):
            if atr.startswith('__') or atr.startswith('id'):
                continue
            setattr(new_peewee_model, atr, getattr(new_model, atr))

        new_peewee_model.save()

        return self.get(id=new_peewee_model.id)


    def get(self, id: int)->dict:
        if self.check_for_errors()['result']:
            return self.check_for_errors()

        res = self.peewee_model.get_or_none(self.peewee_model.id==id)

        return {'code': 200, 'msg': 'Successfully', 'result': res.__data__()} if res else {'code': 400, 'msg': 'Not Found', 'result': None}


    def get_all(self, id: int)->dict:
        if self.check_for_errors()['result']:
            return self.check_for_errors()

        model_list = []

        for model in self.peewee_model.select():
            new_model = {}
            for atr in model.__data__:
                get_atr = getattr(model, atr)
                new_model[atr] = get_atr.id if isinstance(get_atr, peewee.Model) else get_atr

            model_list.append(new_model)

        return {'code': 200, 'msg': 'Successfully', 'result': model_list} if len(model_list) > 0 else {'code': 400, 'msg': 'Not Found', 'result': None}


    def update(self, id: int, new_model: Type[ModifyBaseModel])->dict:
        if self.check_for_errors()['result']:
            return self.check_for_errors()

        res = self.get(id=id)

        if res['code'] != 200:
            return res

        model = self.peewee_model.get(self.peewee_model.id == id)

        for atr in dir(new_model):
            if atr.startswith('__') or atr.startswith('id'):
                continue

            setattr(model, atr, getattr(new_model, atr))

            model.save()

            return {'code': 200, 'msg': 'Successfully', 'result': self.get(id=model.id)['result']}


    def delete(self, id: int)->dict:
        if self.check_for_errors()['result']:
            return self.check_for_errors()

        res = self.get(id=id)

        if res['code'] != 200:
            return res

        self.peewee_model.get(self.peewee_model.id==id).delete_instance()

        return {'code': 200, 'msg': 'Successfully', 'result': None}
