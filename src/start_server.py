from fastapi import FastAPI
from server import routers
from src.server.database.db_manager import db_manager
import uvicorn,settings
from fastapi.responses import RedirectResponse

app = FastAPI(title="Hospital")

[app.include_router(router) for router in routers]

@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == "__main__":
    if not db_manager.check_base():
        db_manager.create_base(settings.CREATE_PATH, settings.FILL_PATH)
    uvicorn.run(app="start_server:app", host=settings.HOST, port=settings.PORT, reload=True)
