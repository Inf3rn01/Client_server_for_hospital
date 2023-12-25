from src.server.database import models as database_models
from src.server.database import pydantic_models
from src.server.service import *


routers = (
    RouterManager(
        database_model=database_models.User,
        pydantic_model=pydantic_models.User,
        prefix='/user',
        tags=['User']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.AuthData,
        pydantic_model=pydantic_models.AuthData,
        prefix='/auth_data',
        tags=['AuthData']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Staff,
        pydantic_model=pydantic_models.Staff,
        prefix='/staff',
        tags=['Staff']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Product,
        pydantic_model=pydantic_models.Product,
        prefix='/product',
        tags=['Product']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.UserOrder,
        pydantic_model=pydantic_models.UserOrder,
        prefix='/user_order',
        tags=['UserOrder']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Discount,
        pydantic_model=pydantic_models.Discount,
        prefix='/discount',
        tags=['Discount']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Storage,
        pydantic_model=pydantic_models.Storage,
        prefix='/storage',
        tags=['Storage']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.UserDiscount,
        pydantic_model=pydantic_models.UserDiscount,
        prefix='/user_discount',
        tags=['UserDiscount']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.StorageOrder,
        pydantic_model=pydantic_models.StorageOrder,
        prefix='/storage_order',
        tags=['StorageOrder']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.ProductInStorage,
        pydantic_model=pydantic_models.ProductInStorage,
        prefix='/product_in_storage',
        tags=['ProductInStorage']
    ).fastapi_router,
)
