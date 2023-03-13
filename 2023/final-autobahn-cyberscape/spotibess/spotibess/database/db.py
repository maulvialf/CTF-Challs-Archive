from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings  import settings
import os

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.DB_USERNAME}:{os.environ.get("DB_PASSWORD")}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Account_DB(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    hashed_password = Column(String)
    email = Column(String)
    is_admin = Column(Boolean, default=False)
    disabled = Column(Boolean, default=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(
        timezone=True), default=func.now(), onupdate=func.current_timestamp())
    
class Audio_DB(Base):
    __tablename__ = 'audio'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    played = Column(Integer)
    namauser = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(
        timezone=True), default=func.now(), onupdate=func.current_timestamp())
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)