from flask import Flask, render_template, request
import urllib.parse
import ipaddress
import re
import http.client
from uuid import UUID

app = Flask(__name__)

def validate_uuid4(uuid_string):
    try:
        val = UUID(uuid_string, version=4)
    except ValueError:
        return False

    return val.hex == uuid_string

def is_valid_ip(ip):
    m = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    return bool(m) and all(map(lambda n: 0 <= int(n) <= 255, m.groups()))

def is_local_ip(hostname):
    forbidden_ip = ["0.0.0.0/8", "127.0.0.1/8"]
    if is_valid_ip(hostname):
        for forbidden in forbidden_ip:
            if ipaddress.ip_address(hostname) in ipaddress.ip_network(forbidden):
                return True 
    
    if hostname == "localhost":
        return True
    
    return False


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fetch", methods=["POST"])
def fetch_gan():
    if request.form.get("host") and request.form.get("is_https") and request.form.get("path") and request.form.get("method"):
        try:
            host = request.form["host"]
            is_https = int(request.form["is_https"])
            method = request.form["method"]
            port = request.form.get("port")
            
            if port:
                port = int(port)
            else:
                port = None

            path = request.form["path"]

            if is_https:
                hostname = urllib.parse.urlparse("https://" + host).hostname
            else:
                hostname = urllib.parse.urlparse("http://" + host).hostname


            if hostname:
                if is_local_ip(hostname):
                    return render_template("index.html", content="You cannot access our internal network")

            if is_https:
                conn = http.client.HTTPSConnection(hostname, port=port, timeout=10)
            else:
                conn = http.client.HTTPConnection(hostname, port=port, timeout=10)
            
            conn.request(method=method, url=path, headers={"User-Agent": "python/http.client"})
            res = conn.getresponse()
            return render_template("index.html", content=res.read().decode())
        except:
            return render_template("index.html", content="There is some internal error, please mind your input !")
        
    else:
        return render_template("index.html", content="required : 'host','is_http','path' and 'method' . optional : 'port'")           


@app.route("/flag")
def flag_home():
    if request.remote_addr == '127.0.0.1':
        admin_header = request.headers.get("admin")
        
        if admin_header:
            admin_header = admin_header.replace("-","")
            if validate_uuid4(admin_header):
                flag = open("this_is_flag.txt").read()
                return flag
            else:
                return "invalid uuid4 'admin' header"
        else:
            return "required : input any valid uuid4 hex for 'admin' header"
    else:
        return "only for internal purpose"