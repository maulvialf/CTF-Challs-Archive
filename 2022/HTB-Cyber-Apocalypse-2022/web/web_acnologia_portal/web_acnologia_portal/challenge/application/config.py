from application.util import generate
import os

class Config(object):
    SECRET_KEY = generate(50)
    UPLOAD_FOLDER = f'{os.getcwd()}/application/static/firmware_extract'
    ADMIN_USERNAME = 'admin'
    ADMIN_PASSWORD = generate(15)
    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'
    SESSION_KEY_PREFIX = ''
    SESSION_FILE_THRESHOLD = 20
    SESSION_USE_SIGNER = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True