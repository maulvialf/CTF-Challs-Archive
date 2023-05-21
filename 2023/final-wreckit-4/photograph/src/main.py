from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from controller import authController, galleryController, profileController, adminController
from controller.authController import cookie_checker
from settings import get_settings
from database.db import get_db
from sqlalchemy.orm import Session
from database.db import engine
from database.conn_pool import database_instance
from fastapi.templating import Jinja2Templates

settings = get_settings()
database_instance = database_instance()

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    openapi_url=""
    )
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )
app.middleware("http")

app.mount("/public", StaticFiles(directory="."), name="public")
app.include_router(authController.router)
app.include_router(galleryController.router)
app.include_router(profileController.router)
app.include_router(adminController.router)

templates = Jinja2Templates(directory="./templates")

@app.exception_handler(Exception)
async def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

@app.on_event("startup")
async def startup():
    await database_instance.connect()

@app.get('/')
async def index(request: Request, db: Session = Depends(get_db)):
    kue = request.cookies.get('user')
    try:
        akun = await cookie_checker(kue, db)
        return templates.TemplateResponse("main.html", {"request": request, "akun": akun})
    except:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":""})