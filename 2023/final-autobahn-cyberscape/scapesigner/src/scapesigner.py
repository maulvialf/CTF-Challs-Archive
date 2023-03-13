#!/usr/bin/env python3
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import base64, functools

b64e = base64.urlsafe_b64encode
b64d = base64.urlsafe_b64decode
mul = lambda arr: functools.reduce(lambda x, y: x * y, arr)


class ScapeSigner:
    def __init__(self, nbit):
        if nbit % 128 != 0 or nbit <= 1024:
            raise ValueError("nbit must be multiple of 128 and > 1024")

        self.set_key_pair(nbit)
        self.check_key_pair()

    def set_key_pair(self, nbit):
        pbit = nbit // 2
        hbit = pbit // 2
        primes = [0]

        while True:
            p = (getRandomNBitInteger(hbit) << (hbit)) + 1
            if isPrime(p) and p.bit_length() == pbit and p > min(primes):
                n = mul(primes := sorted(primes + [p], key=lambda x: -x)[:2])
                if n.bit_length() == nbit:
                    break

        self.n = n
        self.e = 17
        self.d = inverse(self.e, mul(map(lambda x: x - 1, primes)))

    def check_key_pair(self):
        try:
            assert pow(1337, self.e * self.d, self.n) == 1337
        except:
            raise AssertionError("Check failed")

    def get_pubkey(self):
        return RSA.construct((self.n, self.e)).export_key()

    def decrypt(self, msg):
        return b64e(long_to_bytes(pow(bytes_to_long(msg), self.d, self.n)))

    def encrypt(self, sig):
        return long_to_bytes(pow(bytes_to_long(b64d(sig)), self.e, self.n))
