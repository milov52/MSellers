from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
from app.api.routers import main_router
from app.core.config import settings
from app.core.init_db import create_first_superuser


def get_application():
    app = FastAPI(
        title=settings.app_title,
        version=settings.version
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(main_router)
    return app


app = get_application()

# @app.on_event('startup')
# async def startup():
#     await create_first_superuser()


