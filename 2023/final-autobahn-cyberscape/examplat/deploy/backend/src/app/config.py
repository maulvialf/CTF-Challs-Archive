import os
from pathlib import Path


HERE = Path(__file__).parent
SQLITE_PROD = "sqlite:///" + str(HERE / "database.db")


class Config:
    SECRET_KEY = "grsycpljmtyhoycafeiyitsxubxeoapa"
    BCRYPT_LOG_ROUNDS = 4
    TOKEN_EXPIRE_HOURS = 0
    TOKEN_EXPIRE_MINUTES = 0
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SWAGGER_UI_DOC_EXPANSION = "list"
    RESTX_MASK_SWAGGER = False
    JSON_SORT_KEYS = False
    UPLOAD_PATH = "/app/upload"
    EXAM_ANSWER_PATH = "/tmp"


class ProductionConfig(Config):
    TOKEN_EXPIRE_HOURS = 1
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", SQLITE_PROD)
    PRESERVE_CONTEXT_ON_EXCEPTION = True


ENV_CONFIG_DICT = dict(
    production=ProductionConfig
)


def get_config(config_name=None):
    return ENV_CONFIG_DICT.get(config_name, ProductionConfig)
