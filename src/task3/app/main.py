from fastapi import FastAPI

from src.task3.app.core.config import settings
from src.task3.app.core.router import router


def get_app():
    app = FastAPI(
        title=settings.app_name,
    )
    app.include_router(router)

    return app