from src.server.database import models as database_models
from src.server.database import pydantic_models
from src.server.service import *


routers = (
    RouterManager(
        database_model=database_models.Users,
        pydantic_model=pydantic_models.Users,
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
        database_model=database_models.Post,
        pydantic_model=pydantic_models.Post,
        prefix='/post',
        tags=['Post']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Department,
        pydantic_model=pydantic_models.Department,
        prefix='/department',
        tags=['Department']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Role,
        pydantic_model=pydantic_models.Role,
        prefix='/role',
        tags=['Role']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Type_of_disease,
        pydantic_model=pydantic_models.Type_of_disease,
        prefix='/type_of_disease',
        tags=['Type_of_disease']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Type_of_treatment,
        pydantic_model=pydantic_models.Type_of_treatment,
        prefix='/type_of_treatment',
        tags=['Type_of_treatment']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Request,
        pydantic_model=pydantic_models.Request,
        prefix='/request',
        tags=['Request']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Status_request,
        pydantic_model=pydantic_models.Status_request,
        prefix='/status_request',
        tags=['Status_request']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Disease,
        pydantic_model=pydantic_models.Disease,
        prefix='/disease',
        tags=['Disease']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Reception,
        pydantic_model=pydantic_models.Reception,
        prefix='/reception',
        tags=['Reception']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Treatment_status,
        pydantic_model=pydantic_models.Treatment_status,
        prefix='/treatment_status',
        tags=['Treatment_status']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Patients,
        pydantic_model=pydantic_models.Patients,
        prefix='/patients',
        tags=['Patients']
    ).fastapi_router
)
