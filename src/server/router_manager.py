import fastapi
import resolver_manager
from typing import Type
from src.server.database.peewee_models import BaseModel
from src.server.database.pydantic_models import ModifyBaseModel


class RouterManager:

    def __init__(self, peewee_model: Type[BaseModel], pydantic_models: Type[ModifyBaseModel], prefix: str, tags: [str]) -> None:
        self.pydantic_model = pydantic_models
        self.peewee_model = peewee_model
        self.fastapi_router: fastapi.APIRouter = fastapi.APIRouter(prefix=prefix, tags=tags)
        self.resolver_manager = ResolverManager(self.peewee_model,self.pydantic_model)
        self.__init_routers()

    def __init_routers(self):

        @self.fastapi_router.get(path='/get/{id}', response_model=dict)
        def get_record(id: int) -> dict:
            return self.resolver_manager.get(id=id)

        @self.fastapi_router.get(path='/get_all', response_model=dict)
        def get_all_records() -> dict:
            return self.resolver_manager.get_all()
        

        @self.fastapi_router.post(path='/new', response_model=dict)
        def new(new_model: self.pydantic_model) -> dict:
            return self.resolver_manager.new(new_model = new_model)
        
        @self.fastapi_router.put(path='/update/{id}', response_model=dict)
        def update(id: int, new_model: self.pydantic_model) -> dict:
            return self.resolver_manager.update(id, new_model)
        
        @self.fastapi_router.delete(path='/delete/{id}')
        def delete(id: int):
            return self.resolver_manager.delete(id = id)
        