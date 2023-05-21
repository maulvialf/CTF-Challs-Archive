from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, Boolean, ARRAY, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import get_settings
import os

settings = get_settings()
# SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.DB_USERNAME}:{os.environ.get("DB_PASSWORD")}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Account_DB(Base):
    __tablename__ = 'user_person'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    is_admin = Column(Boolean, default=False)
    is_super_admin = Column(Boolean, default=False)
    image = Column(String, default="public/example.svg")
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime( 
        timezone=True), default=func.now(), onupdate=func.current_timestamp())
    
class Photo_DB(Base):
    __tablename__ = 'gallery'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image_path = Column(String)
    description = Column(String)
    visible = Column(Boolean, default=True)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)