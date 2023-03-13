from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.db import Audio_DB
from utilQuery import *

# ------------------------ Schema

class AudioBase(BaseModel):
    name: str
    played: int
    namauser: str

# ------------------------ Class

class Audio():
    name: str
    played: int
    namauser: str

    def create(filename: str, username: str, db: Session):
        audio = Audio_DB(
            name = filename,
            namauser = username,
            played = 0
        )
        db.add(audio)
        db.commit()
        db.refresh(audio) 

        return True

    def is_exist(filename: str, db: Session):
        exist = db.query(Audio_DB).filter(Audio_DB.name == filename).first()
        if exist:
            return True
        else:
            return False
        
    def update_played(filename: str, db: Session):
        file = db.query(Audio_DB).filter(Audio_DB.name == filename).first()
        file.played = file.played + 1
        db.commit()
        db.refresh(file)
        return True

    def get_played(db: Session):
        query = prepare_query('a', 'get-played')
        played = db.execute(query).all()
        print(played)
        res = [[]] * len(played)
        c = 0
        for file in played:
            res[c] = list(file._data)
            c = c + 1
        rest = [{}] * len(res)
        c = 0
        for i in res:
            rest[c] = {"name":i[0], "played":i[1], "number":c+1}
            c = c + 1
        print(rest)
        return rest

    def get_audio_by_name(name: str, db: Session):
        query = prepare_query(name, 'get-audio')
        print(query)
        audios = db.execute(query).all()
        print(audios)
        return audios

    def get_all(db: Session):
        files = db.query(Audio_DB).all()
        print(dir(files))
        return files