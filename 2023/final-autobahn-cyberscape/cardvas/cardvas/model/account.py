from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.db import Account_DB
import bcrypt

# ------------------------ Schema


class AccountBase(BaseModel):
    username: str
    hashed_password: str
    email: str
    is_admin: bool

# ------------------------ Class

class Account():
    username : str
    hashed_password: str
    email: str
    is_admin: bool

    # class Config:
    #     orm_mode = True

    def create(uname: str, eml: str, paswd: str, db: Session):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(paswd.encode(), salt)
        print(hashed)
        akun = Account_DB(
            username = uname,
            hashed_password = hashed.decode(),
            email = eml,
            is_admin = False,
        )
        db.add(akun)
        db.commit()
        db.refresh(akun)

        return True

    def update_picture(name: str, ext: str, db: Session):
        akun = db.query(Account_DB).filter(Account_DB.username == name).first()
        akun.image = name+ext
        db.commit()
        db.refresh(akun)
        return True

    def get_user(email: str, db:Session):
        acc = db.query(Account_DB).filter(Account_DB.email == email).first()
        return acc

    def is_exist(eml: str, db: Session):
        exist = db.query(Account_DB).filter(Account_DB.email == eml).first()
        if not exist:
            return False
        return True
    
    def is_exist_username(uname: str, db: Session):
        exist = db.query(Account_DB).filter(Account_DB.username == uname).first()
        if not exist:
            return False
        return True

    def check_pass(eml: str, pswd: str, db: Session):
        acc = db.query(Account_DB).filter(Account_DB.email == eml).first()
        if bcrypt.checkpw(pswd.encode(), acc.hashed_password.encode()):
            return True
        else:
            return False