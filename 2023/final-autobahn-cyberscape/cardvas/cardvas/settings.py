from typing import Optional
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    DESCRIPTION: str
    VERSION: str
    BACKEND_CORS_ORIGINS: str
    SECRET: str
    DB_TYPE: str
    DB_PORT: str
    DB_HOST: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()