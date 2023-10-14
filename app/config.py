from pydantic_settings import BaseSettings
from .db_requirements import DB_HOST, DB_PORT, DB_NAME, DB_PASS, DB_USER


class Setings(BaseSettings):
    DB_HOST: str = DB_HOST
    DB_PORT: int = DB_PORT
    DB_USER: str = DB_USER
    DB_PASS: str = DB_PASS
    DB_NAME: str = DB_NAME

    @property
    def DATABASE_URL(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Setings()
