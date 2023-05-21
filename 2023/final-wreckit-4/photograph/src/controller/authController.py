from fastapi import APIRouter, Depends, HTTPException, status, Response, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from model.account import Account
from database.db import get_db
from sqlalchemy.orm import Session
from settings import get_settings
from datetime import datetime, timedelta
import jwt
from pydantic import BaseModel
templates = Jinja2Templates(directory="./templates")

settings = get_settings()
router = APIRouter(
    prefix="/auth",
    tags=['auth']
)

class TokenData(BaseModel):
    email: str | None = None
    is_admin: bool | None = None
    id: int | None = None

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET, algorithm=settings.ALGORITHM)
    return encoded_jwt

async def cookie_checker(token : str, db: Session):
    auth = jwt.decode(token, settings.SECRET, algorithms=[settings.ALGORITHM])
    if datetime.fromtimestamp(auth.get("exp")) < datetime.now():
        raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    eml: str = auth.get("sub")
    is_admin: bool = auth.get("is_admin")
    id: int = auth.get("id")
    token_data = TokenData(email=eml, is_admin=is_admin, id=id)
    return token_data # || 1 = 1

@router.post("/regist")
async def regis(request: Request, username: str = Form(), password: str = Form(), email: str = Form(), db : Session = Depends(get_db)):
    if '@' not in email:
        return templates.TemplateResponse("regist.html", {"request": request, "message":"not valid email!"})
    if Account.is_exist(email, db):
        return templates.TemplateResponse("regist.html", {"request": request, "message":"email is registered"})
    if Account.create(username, email, password, db):
        return templates.TemplateResponse("regist.html", {"request": request, "message":"Success"})

@router.post("/login")
async def login(response: Response, password: str = Form(), email: str = Form(), db : Session = Depends(get_db)):
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)  
    if not Account.is_exist(email, db):
        raise HTTPException(status_code=400, detail="Inactive user")
           
    if Account.check_pass(email, password, db):
        akun = Account.get_user(email, db)
        access_token = create_access_token(
            data={"sub": akun.email,  "is_admin": akun.is_admin, "id": akun.id}, expires_delta=access_token_expires
        )
        response = RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
        response.set_cookie(key='user', value=access_token)
        return response
    else:
        print('error')

@router.get("/logout")
async def logout(response: Response):
    response = RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie(key='user')
    return response