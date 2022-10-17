#!/usr/bin/env python3

from Crypto.Util.number import *

m = bytes_to_long(b"slashroot6{ini_bukan_flagnya}")

def try_Decrypt(msg):
    pt = pow(msg,d,n)

    if pt == m:
        return "Tidak ada Takoyaki untukmu"

    return pt

p = getPrime(1024)
q = getPrime(1024)

n = p * q

e = 65537

d = inverse(e, (p-1)*(q-1))

c = pow(m,e,n)

print(f"n : {n}\n")
print(f"e : {e}\n")
print(f"c : {c}")

while True:
    decrypt_ = int(input("\nberikan pesan rahasianya untuk mendapatkan Takoyaki > "))
    res = try_Decrypt(decrypt_)
    print(f"\n[*] pt : {res}")