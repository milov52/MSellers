from fastapi import FastAPI

from backend.app.routers import main_router
from backend.app.config import settings
from backend.app.user.utils import create_first_superuser

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description
)

app.include_router(main_router)


@app.on_event('startup')
async def startup():
    await create_first_superuser()
