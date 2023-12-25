import uvicorn
import fastapi
import settings
from src.server.advanced_import import *


app = fastapi.FastAPI(title='Hospital')

[app.include_router(router) for router in routers]


@app.get('/', include_in_schema=False)
def index() -> fastapi.responses.RedirectResponse:
    return fastapi.responses.RedirectResponse('/docs')


if __name__ == '__main__':
    if settings.DEBUG:
        from src.server.database.db_fill import db_fill
        db_fill()

    uvicorn.run('server:app', reload=True, host=settings.HOST, port=settings.PORT)
