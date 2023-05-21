from fastapi import APIRouter, Depends, HTTPException, status, Response, Form, Request, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from controller.authController import cookie_checker
from error_handler import error_handler
from model.account import Account
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
    prefix="/profile",
    tags=['profile']
)

@router.get('/{id}')
async def get_profile(request: Request, id: int, db: Session = Depends(get_db)):
    template ='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Photograph App</title>
    <link rel="stylesheet" href="main.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<style>
table, th, td{
    border:1px solid black;
}
div.gallery {
  margin: 5px;
  border: 1px solid #ccc;
  float: left;
  width: 180px;
}

div.gallery:hover {
  border: 1px solid #777;
}

div.gallery img {
  width: 100%;
  height: auto;
}

div.desc {
  padding: 15px;
  text-align: center;
}

div.title {
  padding: 1px;
  text-align: center;
}

img {
  width: 100%;
  height: 100%;
}

.bg-black {
  background: #000;
}

.skill-block {
  width: 30%;
}

@media (min-width: 991px) and (max-width:1200px) {
  .skill-block {
    padding: 32px !important;
  }
}

@media (min-width: 1200px) {
  .skill-block {
    padding: 56px !important;
  }
}

body {
  background-color: #eeeeee;
}
</style>
<body>
    <main>
        <a href="../../../../">home</a>
        <a href="../../../../gallery/">gallery</a>
        <a href="../../../../profile/REPLACETHIS">profile</a>
        <a href="../../../../auth/logout">logout</a>
'''
    kue = request.cookies.get('user')
    akun = await cookie_checker(kue, db)
    if akun:
        acc = Account.get_user(akun.email, db)
        template = template.replace('REPLACETHIS',str(akun.id))
        template = template + '''
<div class="container mt-5 mb-5">
    <div class="row no-gutters">
        <div class="col-md-4 col-lg-4"><img src="../../../../../../public/{}"></div>
        <div class="col-md-8 col-lg-8">
            <div class="d-flex flex-column">
                <div class="d-flex flex-row justify-content-between align-items-center p-5 bg-dark text-white">
                    <h3 class="display-5">{}</h3></div>
                <div class="p-3 bg-black text-white">
                    <h6>{}</h6>
                </div>
                <div class="d-flex bg-secondary flex-row text-white">
                    <div class="p-4 bg-success text-center skill-block">
                        <h4>Wanna Change Your Profile Picture?</h4>
                    </div>
                    <div class="p-3 bg-secondary text-center">
                        <form action="../../../../../profile/change-photo/{}" method="post" enctype="multipart/form-data">
                            <div class="container">
                                <label for="picture"><b>Upload photo</b></label>
                                <input type="file" name="picture">
                                <button type="submit">Add</button>
                            </div>
                        </form><br>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</main>
</body>
</html>
        '''.format(acc.image, acc.username, acc.email, acc.id)
        profile_html = open(f'templates/profile/profile_{akun.id}.html', "w")
        profile_html.write(template)
        profile_html.close()
        return templates.TemplateResponse(f"profile/profile_{akun.id}.html", {"request": request})
    else:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":""})
    
@router.post('/change-photo/{id}')
async def change(request: Request, id: int, picture: UploadFile, db: Session = Depends(get_db)):
    kue = request.cookies.get('user')
    akun = await cookie_checker(kue, db)
    if not akun:
        return templates.TemplateResponse("main_lp.html", {"request": request, "message":""})
    
    acc = Account.get_user(akun.email, db)
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

    file_location = f"public/{acc.id}{ext}"
    with open(file_location, "wb+") as file_object:
        file_object.write(picture_data)

    if Account.change_profile(id, file_location, db):
        return RedirectResponse(f"/profile/{id}", status_code=status.HTTP_303_SEE_OTHER)
    else:
        return templates.TemplateResponse("profile.html", {"request": request, "uname":acc.username, "photo":acc.image, "message":"error when upload"})