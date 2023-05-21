from fastapi import APIRouter, Depends, HTTPException, status, Response, Form, Request, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from controller.authController import cookie_checker
from error_handler import error_handler
from model.photo import Photo
from database.db import get_db
from sqlalchemy.orm import Session
from settings import get_settings
import cairosvg
import base64
from urllib.parse import unquote

templates = Jinja2Templates(directory="./templates")
error_handler()

settings = get_settings()
router = APIRouter(
    prefix="/gallery",
    tags=['gallery']
)

@router.get('/')
async def get_all_hardware(request: Request, db: Session = Depends(get_db)):
    kue = request.cookies.get('user')
    akun = await cookie_checker(kue, db)
    if akun:
        list_photo = Photo.get_all(db)
        return templates.TemplateResponse("gallery.html", {"request": request, "datas": list_photo, "akun":akun})
    else:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":""})
    
@router.post('/search')
async def search_photo(request: Request, search: str = Form(), db: Session = Depends(get_db)):
    kue = request.cookies.get('user')
    akun = await cookie_checker(kue, db)
    if akun:
        list_photo = Photo.get_by_search(search, db)
        if not len(list_photo):
            return templates.TemplateResponse("gallery.html", {"request": request, "akun":akun, "msg":"a"})
        return templates.TemplateResponse("gallery.html", {"request": request, "datas": list_photo, "akun":akun})
    else:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":""})

@router.post('/add')
async def add_photo(request: Request, picture: UploadFile, title: str = Form(), desc: str = Form(), db: Session = Depends(get_db)):
    kue = request.cookies.get('user')
    akun = await cookie_checker(kue, db)
    if not akun:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":""})
    elif not akun.is_admin:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":""})
    
    name = picture.filename
    name = unquote(name)
    print(name)
    if 'image/svg' in picture.content_type:
        ext = '.svg'
    elif 'image/png' in picture.content_type:
        ext = '.png'
    elif 'image/jpeg' in picture.content_type:
        ext = '.jpg'
    else:
        raise HTTPException(status_code=400, detail="File type not supported!")

    picture_data = picture.file.read()
    if '.svg' in ext:
        svgdata = picture_data
        pngdata = cairosvg.svg2png(bytestring=svgdata)
        svguri = "data:image/svg+xml;base64," + base64.b64encode(svgdata).decode('utf-8')
        pnguri = "data:image/png;base64," + base64.b64encode(pngdata).decode('utf-8')
        picture_data = pngdata

    if ext == '.svg':
        ext = '.png'

    file_location = f"public/{title}{ext}"
    with open(file_location, "wb+") as file_object:
        file_object.write(picture_data)

    if Photo.create(title, file_location, desc, db):
        return RedirectResponse("/admin", status_code=status.HTTP_303_SEE_OTHER)
    
@router.get("/change/{id}")
async def change_visibility(request: Request, id: int, db: Session = Depends(get_db)):
    kue = request.cookies.get('user')
    akun = await cookie_checker(kue, db)
    if not akun:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":""})
    elif not akun.is_admin:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":""})
    
    if Photo.change_visible(id, db):
        return RedirectResponse("/admin", status_code=status.HTTP_303_SEE_OTHER)
    
@router.get("/delete/{id}")
async def delete(request: Request, id: int, db: Session = Depends(get_db)):
    kue = request.cookies.get('user')
    akun = await cookie_checker(kue, db)
    if not akun:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":""})
    elif not akun.is_admin:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":""})
    
    if Photo.delete(id, db):
        return RedirectResponse("/admin", status_code=status.HTTP_303_SEE_OTHER)