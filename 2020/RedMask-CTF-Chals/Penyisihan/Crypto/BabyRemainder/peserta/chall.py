#!/usr/bin/python
from Crypto.Util.number import bytes_to_long, getPrime, isPrime
from Crypto.Util.Padding import pad
import random

FLAG = open('flag.txt').read().strip()

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def nextPrime(x):
    y = x | 1
    while not isPrime(y) or x == y:
        y += 2
    return y

def func1(m):
    r = 0
    n = getPrime(24)
    for _ in range(20):
        c = m % n
        r = (r + c) << 24
        n = nextPrime(n)
    return r + n

def func2(m):
    e = 65537
    s = int(1.5 * m.bit_length())
    p = getPrime(s)
    q = getPrime(s)
    n = p * q
    phi = (p-1) * (q-1)
    assert gcd(e, phi) == 1
    c = pow(m, e, n)
    return [c, n]

def main():
    m = bytes_to_long(pad(FLAG, 16))
    x = func1(m)
    c, n = func2(m)
    print '[*] x: {}'.format(x)
    print '[*] c: {}'.format(c)
    print '[*] n: {}'.format(n)

if __name__ == "__main__":
    main()
