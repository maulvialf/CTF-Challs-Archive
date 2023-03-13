from fastapi import APIRouter, Depends, HTTPException, UploadFile, Request, status
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from controller.authController import get_current_active_user, cookie_checker
from model.audio import Audio
from model.account import Account
from database.db import get_db
from urllib.parse import unquote
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/audio",
    tags=['audio']
)
templates = Jinja2Templates(directory="./templates")

@router.get('/new')
async def new_audio(request: Request, db: Session = Depends(get_db)):
    kue = request.cookies.get('user')
    username = cookie_checker(kue)
    if username:
        return templates.TemplateResponse("new_audio.html", {"request": request})
    else:
        return templates.TemplateResponse("main.html", {"request": request})

@router.post('/add')
async def add_audio(audio: UploadFile, request: Request, db: Session = Depends(get_db)):
    kue = request.cookies.get('user')
    akun = await cookie_checker(kue, db)
    if not akun:
        return templates.TemplateResponse("main.html", {"request": request})
    name = audio.filename
    name = unquote(name)
    if not '.wav' in name:
        raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail="not wav file!",
            )
    file_location = f"public/{name}"
    with open(file_location, "wb+") as file_object:
        file_object.write(audio.file.read())
    created = Audio.create(name, akun.username, db)
    #print(repr(parsed_xml))
    return RedirectResponse("/audio", status_code=status.HTTP_303_SEE_OTHER)

@router.get('/play/{name}')
async def play_audio(request: Request, name: str, db: Session = Depends(get_db)):
    if not Audio.is_exist(name, db):
        raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail="not in database!",
            )
    if not Audio.update_played(name, db):
        raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail="something happen!",
            )
    return templates.TemplateResponse("audio.html", {"request": request, "name": name})

@router.get('/')
async def get_all_audio(request: Request, db: Session = Depends(get_db)):
    kue = request.cookies.get('user')
    username = await cookie_checker(kue, db)
    lala = Audio.get_audio_by_name(username.username, db)
    print(lala)
    if (kue):
        if (lala):
            return templates.TemplateResponse("index.html", {"request": request, "audios": lala})
        else:
            return templates.TemplateResponse("index.html", {"request": request, "audios": lala})
    else:
        return templates.TemplateResponse("main.html", {"request": request})
    # return lala