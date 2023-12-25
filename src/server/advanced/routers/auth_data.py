from src.server.router import routers
from src.server.database.pydantic_models import LoginData
from fastapi import FastAPI
from src.server.advanced.resolvers import auth_data


user_router: FastAPI = routers[1]


@user_router.post('/login', response_model=int | dict)
def login(login_data: LoginData) -> int | dict:
    return auth_data.login(login_data.login, login_data.password)
