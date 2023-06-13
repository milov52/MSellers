from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Управление продажами в маркетплейсках'
    secret: str = 'SECRET'
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    @property
    def database_url(self):
        prefix = 'postgresql+asyncpg://'
        user = f"{self.DB_USER}:{self.DB_PASS}"
        database = f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        print(prefix + user + "@" + database)
        return prefix + user + "@" + database

    class Config:
        env_file = '.env'


settings = Settings()
