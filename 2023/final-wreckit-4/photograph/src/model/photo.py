from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.db import Photo_DB
from query_handler import *

# ------------------------ Schema


class PhotoBase(BaseModel):
    name: str
    image_path: str
    description: str
    visible: bool

# ------------------------ Class

class Photo():
    name: str
    image_path: str
    description: str
    visible: bool

    def create(uname: str, path: str, desc: str, db: Session):
        photo = Photo_DB(
            name = uname,
            image_path = path,
            description = desc
        )
        db.add(photo)
        db.commit()
        db.refresh(photo)
        db.close()
        return True
    
    def get_all(db: Session):
        items = db.query(Photo_DB).filter(Photo_DB.visible == True).all()
        db.close()
        return items
    
    def get_all_admin(db: Session):
        items = db.query(Photo_DB).all()
        db.close()
        return items
    
    def change_visible(id: int, db: Session):
        photo = db.query(Photo_DB).filter(Photo_DB.id == id).first()
        if photo.visible:
            photo.visible = False
        else:
            photo.visible = True
        
        db.commit()
        db.refresh(photo)
        db.close()
        return True

    def get_by_search(txt: str, db: Session):
        query = prepare_query(txt, 'get-photo')
        print(query)
        audios = db.execute(query).all()
        print(audios)
        return audios
    
    def delete(id: int, db: Session):
        item = db.query(Photo_DB).filter(Photo_DB.id == id).delete()
        db.commit()
        db.close()
        return True