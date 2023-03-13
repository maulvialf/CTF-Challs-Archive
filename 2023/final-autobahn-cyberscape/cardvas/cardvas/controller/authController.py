from fastapi import APIRouter, Depends, HTTPException, status, Response, Form, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from settings import settings
from datetime import datetime, timedelta
import jwt
from model.account import Account
from database.db import get_db
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import urllib
import os
templates = Jinja2Templates(directory="./templates")

router = APIRouter(
    prefix="/auth",
    tags=['auth']
)

class UserInDB(Account):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class CustomURLProcessor:
    def __init__(self):  
        self.path = "" 
        self.request = None

    def url_for(self, request: Request, name: str, **params: str):
        self.path = request.url_for(name, **params)
        self.request = request
        return self
    
    def include_query_params(self, **params: str):
        parsed = list(urllib.parse.urlparse(self.path))
        parsed[4] = urllib.parse.urlencode(params)
        return urllib.parse.urlunparse(parsed)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.environ.get("SECRET"), algorithm=settings.ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    auth = jwt.decode(token, os.environ.get("SECRET"), algorithms=[settings.ALGORITHM]) 
    if datetime.fromtimestamp(auth.get("exp")) < datetime.now():
        raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    username: str = auth.get("sub")
    user = Account.get_user(username, db)
    return user

async def get_current_active_user(current_user: Account = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

async def cookie_checker(token : str, db: Session):
    auth = jwt.decode(token, os.environ.get("SECRET"), algorithms=[settings.ALGORITHM])
    if datetime.fromtimestamp(auth.get("exp")) < datetime.now():
        raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    eml: str = auth.get("sub")
    user = Account.get_user(eml, db)
    return user # || 1 = 1

@router.post("/regist")
async def regis(request: Request, response: Response, username: str = Form(), password: str = Form(), email: str = Form(), db : Session = Depends(get_db)):
    if Account.is_exist(email, db):
        return {"msg":"email is registered"}
    if Account.create(username, email, password, db):
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES) 
        access_token = create_access_token(
            data={"sub": email}, expires_delta=access_token_expires
        )
        redirect_url = CustomURLProcessor().url_for(request, 'get_card').include_query_params(msg="Succesfully created!")
        response = RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
        response.set_cookie(key='user', value=access_token)
        return response

@router.post("/login")
async def login(response: Response, password: str = Form(), email: str = Form(), db : Session = Depends(get_db)):
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)  
    if not Account.is_exist(email, db):
        raise HTTPException(status_code=400, detail="Inactive user")
           
    if Account.check_pass(email, password, db):
        akun = Account.get_user(email, db)
        access_token = create_access_token(
            data={"sub": akun.email}, expires_delta=access_token_expires
        )
        response = RedirectResponse("/card", status_code=status.HTTP_303_SEE_OTHER)
        response.set_cookie(key='user', value=access_token)
        return response
    else:
        print('error')

@router.post("/token", response_model=Token)
async def token(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    data = form_data
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)  
    if not Account.is_exist(data.username, db):
        raise HTTPException(status_code=400, detail="Inactive user")
           
    if Account.check_pass(data.username, data.password, db):
        access_token = create_access_token(
            data={"sub": data.username}, expires_delta=access_token_expires
        )
        print('dud', access_token)
        response.set_cookie(key='access_token', value=access_token)
        response.set_cookie(key="token_type", value="bearer")
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        print('error')