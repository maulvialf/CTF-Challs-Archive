from fastapi import APIRouter, Depends, HTTPException, status, Response, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from controller.authController import cookie_checker
from model.photo import Photo
from model.account import Account
from database.db import get_db
from sqlalchemy.orm import Session
from settings import get_settings
templates = Jinja2Templates(directory="./templates")

settings = get_settings()
router = APIRouter(
    prefix="/admin",
    tags=['admin']
)

@router.get('/')
async def get_all_hardware(request: Request, db: Session = Depends(get_db)):
    kue = request.cookies.get('user')
    akun = await cookie_checker(kue, db)
    if not akun:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":""})
    elif not akun.is_admin:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":"plis login using admin account"})
    
    list_photo = Photo.get_all_admin(db)
    return templates.TemplateResponse("admin_conf.html", {"request": request, "datas": list_photo, "akun": akun})
    
@router.get('/console')
async def console_psql(request: Request, db: Session = Depends(get_db)):
    kue = request.cookies.get('user')
    akun = await cookie_checker(kue, db)
    if not akun:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":""})
    elif not akun.is_admin:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":"plis login using admin account"})
    
    super_admin = Account.get_user(akun.email, db).is_super_admin
    if not super_admin:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":"plis login using super admin account"})
    
    return templates.TemplateResponse("console.html", {"request": request, "akun":akun})

@router.post('/console')
async def console_psql(request: Request, query: str = Form(), db: Session = Depends(get_db)):
    kue = request.cookies.get('user')
    akun = await cookie_checker(kue, db)
    if not akun:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":""})
    elif not akun.is_admin:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":"plis login using admin account"})
    
    super_admin = Account.get_user(akun.email, db).is_super_admin
    if not super_admin:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":"plis login using super admin account"})
    
    res = Account.super_admin(query, db)
    return templates.TemplateResponse("console.html", {"request": request, "res": res, "akun":akun})