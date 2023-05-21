from typing import Optional
from pydantic import BaseSettings
from functools import lru_cache

class settings(BaseSettings):
    VERSION="1"
    APP_NAME : str
    DESCRIPTION : str
    SECRET : str
    VERSION : str
    BACKEND_CORS_ORIGINS : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int

    DB_TYPE : str
    DB_PORT : str
    DB_HOST : str
    DB_USERNAME : str
    DB_NAME : str

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return settings()