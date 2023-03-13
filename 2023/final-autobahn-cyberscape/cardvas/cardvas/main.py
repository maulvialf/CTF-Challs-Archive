from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from controller import authController, cardController
from settings import settings
from database.db import engine
from database.conn_pool import database_instance
from fastapi.templating import Jinja2Templates

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

app.mount("/public", StaticFiles(directory="public"), name="public")
app.include_router(authController.router)
app.include_router(cardController.router)

templates = Jinja2Templates(directory="./templates")

@app.exception_handler(Exception)
async def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    # Change here to LOGGER
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

@app.on_event("startup")
async def startup():
    await database_instance.connect()
    app.state.db = database_instance

@app.get('/')
async def index(request: Request):
    # print('masuk', flush=True)
    # return {"msg":"Hello! Welcome to API."}
    return templates.TemplateResponse("main.html", {"request": request})