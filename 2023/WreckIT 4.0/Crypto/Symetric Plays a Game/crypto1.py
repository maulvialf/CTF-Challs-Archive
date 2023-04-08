#!/usr/bin/python3
from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from redacted import flag 
import os

#i will give hint is too simple,
fakeG = b'WRECKIT20{satu_masalah_ini_lagi_jangan_tertipu}'

def encrypt(plaintext):
    keys = os.urandom(32)
    added = 0
    print('fake flag is = '+ fakeG.decode())
    added = int(input('add the fake flag number: '))
    fake = fakeG + long_to_bytes(added)
    plaintext = long_to_bytes(plaintext)
    pad1 = pad(plaintext + flag, 16)
    pad2 = pad(fake + flag, 16)
    iv = 16 * b'\x00'
    cipher1 = AES.new(keys, AES.MODE_CBC, iv)
    cipher2 = AES.new(keys, AES.MODE_CBC, iv)
    try:
        enc1 = cipher1.encrypt(pad1)
        enc2 = cipher2.encrypt(pad2)
    except ValueError as e:
        return {"error": str(e)}
    
    return (enc1.hex(),enc2.hex())

inc = 0
while True:
    inp = int(input('choose your number bigger than 16= '))
    if(inp<16):
        print("you are in violation of the rules, thanks ...")
        break
    print(encrypt(inp))
    inc+=1
    if(inc==5000):
        print("I'm so sorry, You reach the limits")
        break
