from flask import Flask, render_template, request
import os

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/admin_gan", methods=["POST"])
def adminonly():
    admin_header = request.headers.get("X-Admin")
    action = request.form.get("action")
    value = request.form.get("value")
    secret = open("f4pl1bvsqQ.txt").read()

    if action == "1":
        if os.path.isdir(value) and admin_header == secret:
                return str(os.listdir(value))
        else:
            return "You must pass all the requirements to listing a directory"
    elif action == "2":
        if os.path.isfile(value) and admin_header == secret:
                return open(value).read()
        else:
            return "You must pass all the requirements to read a file"
    else:
        return action