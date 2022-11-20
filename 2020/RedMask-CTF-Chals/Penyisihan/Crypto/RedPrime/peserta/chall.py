#!/usr/bin/python
from Crypto.Util.number import *
from fractions import Fraction
from flag import flag

def calc(a, b, c):
    s = float(a if b else -a)
    while True:
        s *= -c
        a += s
        if abs(s) < .0001:
            return int(a) + 1

def genPrime(nbit):
    while True:
        x = getRandomNBitInteger(nbit)
        p = calc(x, False, Fraction(11, 17))
        q = calc(x, True, Fraction(13, 19))
        if isPrime(p) and isPrime(q):
            return p, q

def encrypt(m, n):
    m = bytes_to_long(m)
    assert m < n
    return pow(m, 65537, n)

nbit = 512
p, q = genPrime(nbit)
n = p * q
c = encrypt(flag, n)

print 'c =', c
print 'n =', n
