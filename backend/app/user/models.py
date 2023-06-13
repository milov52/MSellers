from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from backend.app.database import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    pass
