#!/usr/bin/env python3
from Crypto.Util.number import *

FLAG = open('flag.txt', 'rb').read()


def gen_key(e):
    while True:
        p = getPrime(1024)
        q = getPrime(1024)

        if GCD(e, p - 1) != 1:
            n = p * q
            x = (p | q) & (~p | ~q)

            return x, n


e = 17
x, n = gen_key(e)

m = bytes_to_long(FLAG)
c = pow(m, e, n)

print(f"e = {e}")
print(f"x = {x}")
print(f"n = {n}")
print(f"c = {c}")
