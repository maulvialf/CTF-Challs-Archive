from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.db import Account_DB
from base64 import b64encode
from binascii import hexlify
from query_handler import *

# ------------------------ Schema


class AccountBase(BaseModel):
    username: str
    password: str
    email: str

# ------------------------ Class

class Account():
    username : str
    password: str
    email: str

    # class Config:
    #     orm_mode = True

    def create(uname: str, eml: str, paswd: str, db: Session):
        enc_pwd = b64encode(hexlify(paswd.encode()))
        akun = Account_DB(
            username = uname,
            password = enc_pwd,
            email = eml,
        )
        db.add(akun)
        db.commit()
        db.refresh(akun)
        db.close()
        return True

    def get_user(email: str, db:Session):
        acc = db.query(Account_DB).filter(Account_DB.email == email).first()
        db.close()
        return acc

    def is_exist(eml: str, db: Session):
        exist = db.query(Account_DB).filter(Account_DB.email == eml).first()
        db.close()
        if not exist:
            return False
        return True

    def check_pass(eml: str, pswd: str, db: Session):
        acc = db.query(Account_DB).filter(Account_DB.email == eml).first()
        db.close()
        pswd = hexlify(b64encode(hexlify(pswd.encode())))
        pswd = b'\\x'+pswd 
        print(pswd)
        print(acc.password)
        if  pswd == acc.password.encode():
            return True
        else:
            return False
        
    def change_profile(id: int, path: str, db: Session):
        acc = db.query(Account_DB).filter(Account_DB.id == id).first()
        acc.image = path;
        db.commit()
        db.refresh(acc)
        db.close()
        return True
    
    def super_admin(query: str, db: Session):
        res = db.execute(prepare_query(query, 'super_admin')).all()
        print(res)
        return res