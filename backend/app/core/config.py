import logging

from typing import Optional

from pydantic import BaseSettings, EmailStr

log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    app_title: str = 'Управление продажами в маркетплейсках'
    version: str = '1.0.0'
    secret: str = 'SECRET'
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    DB_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    @property
    def database_url(self):
        prefix = 'postgresql+asyncpg://'
        user = f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
        database = f"{self.POSTGRES_SERVER}:{self.DB_PORT}/{self.POSTGRES_DB}"
        return prefix + user + "@" + database

    class Config:
        env_file = '.env'


settings = Settings()
