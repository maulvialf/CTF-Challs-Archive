#!/usr/bin/python3

import random
import os
from Crypto.Cipher import AES
from os import urandom
from string import printable
from binascii import hexlify

random.seed(urandom(32))

key1 = b'0'*13 + b''.join([random.choice(printable).encode() for _ in range(3)])
key2 = b''.join([random.choice(printable).encode() for _ in range(3)]) + b'0'*13
IV = os.urandom(16)

def xor(a, b):
    return b"".join([chr(x^y).encode("latin1") for x,y in zip(a,b)])

def natsu(plaintext1):
    cipher1 = AES.new(key=key1, mode=AES.MODE_ECB)
    c1 = cipher1.encrypt(hexlify(plaintext1))
    return c1

def dragneel(plaintext3):
    cipher3 = AES.new(key=key2, mode=AES.MODE_ECB)
    c2 = b""
    plaintext_block = [plaintext3[i:i+16] for i in range(0,len(plaintext3),16)]
    init = IV
    for block in plaintext_block:
        ciphertext_block = cipher3.encrypt(init)
        result = xor(ciphertext_block, block)
        c2 += result
        init = ciphertext_block
    return c2

flag = open("flag.txt", "rb").read().strip()
enc_flag = natsu(dragneel(hexlify(flag)))
print(f"Your flag is: {hexlify(IV).decode('latin1') + hexlify(enc_flag).decode('latin1')}")

while True:
    print("\n")
    print("Menu:")
    print("[1] Encrypt message")
    print("[2] Exit")
    inp = input("Input: ")
    
    if inp == "1":
        pt = input("your message : ").encode("latin1")
        val = len(pt) % 16
        if not val == 0:
            pt += b'0'*(16 - val)
        enc = natsu(dragneel(hexlify(pt)))
        print(f"Your encrypted message is: {hexlify(IV).decode('latin1') + hexlify(enc).decode('latin1')}")
    elif inp == "2":
        exit()
    else:
        print("Unknown input...")
    print()