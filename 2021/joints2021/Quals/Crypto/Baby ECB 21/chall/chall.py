#!/usr/bin/python2
from Crypto.Cipher import AES
from secret import flag
import json
from os import urandom
import sys
import os
from hashlib import md5
import datetime


class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


sys.stdout = Unbuffered(sys.stdout)

KEY = os.urandom(16)
BS = 16
def pad(s): return s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
def unpad(s): return s[:-ord(s[len(s)-1:])]


class AESCipher(object):
    def __init__(self, key):
        self.key = key

    def encrypt(self, plain):
        message = pad(plain)
        obj = AES.new(self.key, AES.MODE_ECB)
        cipher = obj.encrypt(message)
        return cipher.encode('hex')

    def decrypt(self, cipher):
        cipher = cipher.decode('hex')
        obj = AES.new(self.key, AES.MODE_ECB)
        plain = obj.decrypt(cipher)
        return unpad(plain)


def getData(token):
    token = obj.decrypt(token)
    data = json.loads(token)
    return data


def removeEscapeChar(data):
    text = ''
    for char in data:
        if char == '\\':
            continue
        text += char
    return text


def checkToken():
    token = raw_input('Token: ')
    data = getData(token)

    return data


if __name__ == '__main__':
    while True:
        now = datetime.datetime.now()
        expiredToken = (now + datetime.timedelta(minutes=30)).strftime('%s')

        print("=== Register ===")
        name = raw_input("Your name: ")

        data = {
            "alias": name,
            "is_admin": 0,
            "encryption_alg": "AES MODE_ECB",
        }

        m = removeEscapeChar(json.dumps(data))
        obj = AESCipher(KEY)
        token = obj.encrypt(m)

        print("Token : {}".format(token))
        print("""
1). Login with token
2). Get Flag
3). Register
4). Exit
        """
              )
        try:
            choice = int(raw_input(">> "))
            if choice == 1:
                data = checkToken()
                print("Welcome {}".format(data['alias']))
                print("Login successful")
                os._exit(1)
            elif choice == 2:
                data = checkToken()
                if(not data["is_admin"]):
                    print('Unauthorized Access')
                else:
                    print(flag)
                os._exit(1)
            elif choice == 3:
                continue
            else:
                os._exit(1)
            print
            print
        except:
            print('Error Occurred')
            exit(0)
