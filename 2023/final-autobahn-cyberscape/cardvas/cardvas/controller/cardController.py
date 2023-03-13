from fastapi import APIRouter, Depends, HTTPException, status, Response, Form, Request, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from defusedxml import ElementTree
from controller.authController import cookie_checker
from database.db import get_db
from sqlalchemy.orm import Session
from urllib.parse import unquote
from model.account import Account
from settings import settings
import cairosvg
import base64
import urllib
templates = Jinja2Templates(directory="./templates")

router = APIRouter(
    prefix="/card",
    tags=['card']
)

@router.post('/change')
async def change_picture(request: Request, picture: UploadFile, db: Session = Depends(get_db)):
    template = '''
        <html>
        <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
        .card {
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        max-width: 300px;
        margin: auto;
        text-align: center;
        font-family: arial;
        }

        .title {
        color: grey;
        font-size: 18px;
        }

        .buttonas {
        border: none;
        outline: 0;
        display: inline-block;
        padding: 8px;
        color: white;
        background-color: #000;
        text-align: center;
        cursor: pointer;
        width: 100%;
        font-size: 18px;
        }

        a {
        text-decoration: none;
        font-size: 22px;
        color: black;
        }

        .buttonas:hover, a:hover {
        opacity: 0.7;
        }

        body {
        padding: 20px;
        }
        </style>
        </head>
        <body>

        <h2 style="text-align:center">User Profile Card</h2>
        '''
    kue = request.cookies.get('user')
    akun = await cookie_checker(kue, db)
    if not akun:
        return templates.TemplateResponse("main.html", {"request": request})
    name = picture.filename
    print(picture)
    print(picture.content_type)
    name = unquote(name)
    if 'image/svg' in picture.content_type:
        ext = '.svg'
    elif 'image/png' in picture.content_type:
        ext = '.png'
    elif 'image/jpeg' in picture.content_type:
        ext = '.jpg'
    else:
        raise HTTPException(status_code=400, detail="File type not supported!")

    file_location = f"public/{akun.username}{ext}"
    picture_data = picture.file.read()
    with open(file_location, "wb+") as file_object:
        file_object.write(picture_data)
    if Account.update_picture(akun.username, ext, db):
        file = f'../../public/{akun.username}{ext}'
        print(file)
        template = template + '''
        <div class="card">
        <img src="{}" alt="{}" style="width:100%">
        <h1>{}</h1>
        <p><button class="buttonas">{}</button></p>
        </div>

        <h2>Wanna Change your Picture?</h2>
        <form action="/card/change" method="post" enctype="multipart/form-data">
            <input type="file" name="picture"><br>
            <button type="submit">Add</button>
        </form>
        '''.format(file, akun.username, akun.username, akun.email)

        if '.svg' not in ext:
            template = template + '''
            </body>
            </html>
            '''
            card_html = open('templates/cardd.html', "w")
            n = card_html.write(template)
            card_html.close()
            return templates.TemplateResponse("cardd.html", {"request": request})

        svgdata = picture_data
        pngdata = cairosvg.svg2png(bytestring=svgdata)
        
        svguri = "data:image/svg+xml;base64," + base64.b64encode(svgdata).decode('utf-8')
        pnguri = "data:image/png;base64," + base64.b64encode(pngdata).decode('utf-8')
        template = template + '''
            <h2>SVG Representation</h2>
            <div><img src="{}"></div>
            <h2>PNG Representation</h2>
            <div><img src="{}"></div>
        </body>
        </html>
        '''.format(svguri, pnguri)
        card_html = open('templates/cardd.html', "w")
        n = card_html.write(template)
        card_html.close()
        return templates.TemplateResponse("cardd.html", {"request": request})

def error_handler():
    def external_handler(parser, context, base, sysid, pubid):
        print('parser: {}\ncontext: {}\nbase: {}\nsysid: {}\npubid: {}\n'.format(
            parser, context, base, sysid, pubid))
        data = urllib.request.urlopen(sysid).read()
        child = parser.parser.ExternalEntityParserCreate(context)
        child.Parse(data)
        return 1

    d = ElementTree.DefusedXMLParser
    d.defused_entity_decl = None
    d.defused_unparsed_entity_decl = None
    d.defused_external_entity_ref_handler = external_handler

@router.get('/')
async def get_card(request: Request, db: Session = Depends(get_db)):
    kue = request.cookies.get('user')
    username = await cookie_checker(kue, db)
    template = '''
        <html>
        <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
        .card {
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        max-width: 300px;
        margin: auto;
        text-align: center;
        font-family: arial;
        }

        .title {
        color: grey;
        font-size: 18px;
        }

        .buttonas {
        border: none;
        outline: 0;
        display: inline-block;
        padding: 8px;
        color: white;
        background-color: #000;
        text-align: center;
        cursor: pointer;
        width: 100%;
        font-size: 18px;
        }

        a {
        text-decoration: none;
        font-size: 22px;
        color: black;
        }

        .buttonas:hover, a:hover {
        opacity: 0.7;
        }

        body {
        padding: 20px;
        }
        </style>
        </head>
        <body>

        <h2 style="text-align:center">User Profile Card</h2>
        '''
    if username:
        if username.is_admin:
            file = f'public/{username.image}'
        else:
            file = f'../../public/{username.image}'
            template = template + '''
            <div class="card">
            <img src="{}" alt="{}" style="width:100%">
            <h1>{}</h1>
            <p><button class="buttonas">{}</button></p>
            </div>

            <h2>Wanna Change your Picture?</h2>
            <form action="/card/change" method="post" enctype="multipart/form-data">
                <input type="file" name="picture"><br>
                <button type="submit">Add</button>
            </form>

            </body>
            </html>
            '''.format(file, username.username, username.username, username.email)
            card_html = open('templates/cardd.html', "w")
            n = card_html.write(template)
            card_html.close()
            
            # return templates.TemplateResponse(template, {"request":request})
            return templates.TemplateResponse("cardd.html", {"request": request, "data": file, "name": username.username, "email": username.email})
    else:
        return templates.TemplateResponse("main.html", {"request": request})
    
error_handler()