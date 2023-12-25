import uvicorn
import fastapi
import settings
from src.server.advanced_import import *


app = fastapi.FastAPI(
    title='PharmancyEnt api',
    version='1.0 Server',
    description='PharamancyEntAPI - PharamancyEnt Application Programming Interface'
)

[app.include_router(router) for router in routers]


@app.get('/', include_in_schema=False)
def index() -> fastapi.responses.RedirectResponse:
    return fastapi.responses.RedirectResponse('/docs')


if __name__ == '__main__':
    if settings.DEBUG:
        from src.server.database.db_fill import db_fill
        db_fill()

    uvicorn.run('server:app', reload=True, host=settings.SERVER_HOST, port=settings.SERVER_PORT)
