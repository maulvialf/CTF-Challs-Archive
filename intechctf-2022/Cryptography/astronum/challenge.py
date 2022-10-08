#!/usr/bin/python3
import os
from hashlib import sha256
from random import randint
from Crypto.Util.number import bytes_to_long, GCD, inverse

SAFE_PRIME = 151258274681755280143813939193016075988615876757803336743621456130914928145410166816556181133906067470486021613268137173047293000953352393489740467147541163493656909601795971958653990476387134915485093480453204696595185037088237739275367534252317760493882850232819497555751442035215626885702967752104806735491


class TTD:

    def __init__(self, p, g):
        self.p = p
        self.g = g

        self.x = randint(2, p - 2)
        self.y = pow(self.g, self.x, self.p)

    def sign(self, m):
        while True:
            h = bytes_to_long(sha256(m).digest())
            k = randint(2, self.p - 2)
            if GCD(k, self.p - 1) != 1:
                continue
            r = pow(self.g, k, self.p)
            s = (h - self.x * r) * inverse(k, self.p - 1) % (self.p - 1)
            if s == 0:
                continue
            return (hex(r), hex(s))

    def verify(self, m, r, s):
        if (r < 1 or s < 1) and (r > self.p or s > self.p):
            return False

        h = bytes_to_long(sha256(m).digest())

        u1 = pow(self.g, h, self.p)
        u2 = (pow(self.y, r, self.p) * pow(r, s, self.p)) % self.p

        return u1 == u2


signer = TTD(SAFE_PRIME, 3)
FLAG = open('flag.txt', 'rb').read()

if __name__ == "__main__":
    secret = os.urandom(32)
    print(f"My public key: {signer.y}")

    while True:
        print("=" * 15)
        print("[1] Register")
        print("[2] Authenticate")
        print("[3] Exit")
        op = input(">> ")

        if op == "1":
            username = input("Enter username: ")
            if username == "admin":
                print("Username \"admin\" not available")
                break
            else:
                signature = signer.sign(username.encode())
                print(f"Your signature: {signature}")
        elif op == "2":
            username = input("Enter username: ")
            print("Please, input your signature to authenticate")
            r = int(input("r: "), 16)
            s = int(input("s: "), 16)

            try:
                if signer.verify(username.encode(), r, s):
                    print("Signature valid")
                    print("Welcome, " + username)

                    if username == "admin":
                        print(FLAG)

                    break
                else:
                    print("Invalid signature")
                    break
            except Exception as e:
                print(e)
                print("Invalid signature")
                break
        else:
            break
