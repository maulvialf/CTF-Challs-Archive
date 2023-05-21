from flask import Flask, request
from Crypto.Cipher import AES
from Crypto.Util.number import *
from Crypto.Util.Padding import pad
import json
import math
import random
import time

app = Flask(__name__)

class EncryptionScheme:
    def iniT(self):
        seedTime = int(time.time()*100)%10000
        random.seed(seedTime)
        checkNumber = random.getrandbits(512)
        line = b"+FLAGPOINT+"
        flagpoint = bytes_to_long(flag+line+str(seedTime).encode())
        return flagpoint, line, checkNumber

    def getprimes(self, x):
        prime = x
        if(not prime&1): prime+=1
        while(not isPrime(prime)): prime+=2
        return prime

    def asyRaSA(self, m, flg):
        p = self.getprimes(random.getrandbits(512))
        q = self.getprimes(p+512)
        print(p, q)
        phi = (p-1)*(q-1)
        n = p*q
        d = bytes_to_long(flg)
        x = 0
        while(math.gcd(d, phi)!=1):
            x += 1
            d+=1
        print(d)
        print("loop ", x)
        e = pow(d, -1, phi)
        c = pow(m, e, n)
        return c, e, n

    def MerAeS(self, m, c):
        keys = flag[:32]
        iv = pad(long_to_bytes(c)[:4],16)
        cipher = AES.new(keys, AES.MODE_CBC, iv)
        ct = cipher.encrypt(pad(m, 16))
        return bytes_to_long(ct)

def encrypt(msg):
    global flag
    flag = open("flag.txt", "rb").read()
    enc = EncryptionScheme()
    flagpoint, line, checkNumber = enc.iniT()
    
    c, e, n = enc.asyRaSA(flagpoint, flag)
    ct = enc.MerAeS(msg+flag, c)
    result = {
        "line": line.decode(),
        "checkNumber": hex(checkNumber),
        "c": hex(c),
        "e": hex(e),
        "n": hex(n),
        "ct": hex(ct),
        "iv": hex(c),
    }
    return result

@app.route("/encrypt", methods=["POST"])
def encryption():
    getdata = request.get_json()
    message = bytes.fromhex(getdata["plaintext"])
    result = encrypt(message)
    return json.dumps(result, indent=2)

@app.route("/", methods=["GET"])
def home():
    return "This is encryption server"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
