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
    disabled: bool


# ------------------------ Class

class Account():
    username : str
    hashed_password: str
    email: str
    is_admin: bool
    disabled: bool  

    def create(uname: str, eml: str, paswd: str, db: Session):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(paswd.encode(), salt)
        print(hashed)
        akun = Account_DB(
            username = uname,
            hashed_password = hashed.decode(),
            email = eml,
            is_admin = False,
            disabled = False
        )
        db.add(akun)
        db.commit()
        db.refresh(akun)

        return True

    def get_user(email: str, db:Session):
        acc = db.query(Account_DB).filter(Account_DB.email == email).first()
        return acc

    def is_exist(eml: str, db: Session):
        print(eml)
        exist = db.query(Account_DB).filter(Account_DB.email == eml).first()
        print(exist)
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
        print(acc)
        if bcrypt.checkpw(pswd.encode(), acc.hashed_password.encode()):
            return True
        else:
            return False