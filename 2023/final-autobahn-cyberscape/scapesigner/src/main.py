#!/usr/bin/env python3
from flask import Flask, make_response, render_template, request
from scapesigner import ScapeSigner
import hashlib, json, sqlite3, time


app = Flask(__name__)
db = "database.db"
get_db_con = lambda: sqlite3.connect(db)
html = "index.html"
signer = ScapeSigner(1536)


def generate_token(username, role):
    user = {"username": username, "role": role, "expired": 5 * 60 + int(time.time())}
    token = signer.decrypt(json.dumps(user).encode())
    return token.decode()


def validate_token(token):
    user = json.loads(signer.encrypt(token))
    assert int(user.get("expired")) > int(time.time())
    if user.get("role") == "admin":
        return f"Welcome, {user['username']}! {open('/flag/flag.txt').read()}"
    else:
        return f"Dear {user['username']}, only admin can access the flag"


def get_role(username, password):
    con = get_db_con()
    cur = con.cursor()
    cur.execute(
        "SELECT role FROM users WHERE username = ? AND password = ?",
        (username, hashlib.sha256(password.encode()).hexdigest()),
    )
    role = cur.fetchone()
    con.close()
    assert role
    return role[0]


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        try:
            assert 2 <= len(username) <= 32
            assert 2 <= len(password) <= 32
            role = get_role(username, password)
            token = generate_token(username, role)
            response = make_response(render_template(html, data=validate_token(token)))
            response.set_cookie("token", token)
            return response
        except:
            return "Invalid username and/or password"
    else:
        token = request.cookies.get("token")
        if token:
            try:
                return render_template(html, data=validate_token(token))
            except:
                return "Invalid token"
        else:
            return render_template(html)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
