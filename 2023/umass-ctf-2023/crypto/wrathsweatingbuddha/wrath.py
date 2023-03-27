#!/usr/bin/env python3
#
# Polymero
#

# Imports
from Crypto.Util.number import getPrime, GCD, inverse
from secrets import randbelow
import base64

# Local imports
with open("flag.txt", "rb") as f:
    FLAG = f.read()[::-1]
    f.close()


class Buddhier:
    def __init__(self):
        P, Q = [getPrime(512) for _ in range(2)]
        self.N = P * Q
        self.G = randbelow(self.N * self.N)
        self.L = (P - 1) * (Q - 1) // GCD(P - 1, Q - 1)
        self.U = inverse((pow(self.G, self.L, self.N * self.N) - 1) // self.N, self.N)

    def encrypt(self, msg: int) -> int:
        g_m = pow(self.G, msg, self.N * self.N)
        r_n = pow(randbelow(self.N), self.N, self.N * self.N)
        return (g_m * r_n) % (self.N * self.N)

    def decrypt(self, cip: int) -> int:
        msg = ((pow(cip, self.L, self.N * self.N) - 1) // self.N * self.U) % self.N
        return msg

    def barter(self, cip: int) -> int:
        k = self.decrypt(cip) & 1
        r = randbelow(self.N)
        rG = pow(r, randbelow(self.N), self.N * self.N)
        g_m = pow(rG, k + 1, self.N * self.N)
        r_n = pow(r, self.N, self.N * self.N)
        return (g_m * r_n) % (self.N * self.N)


bud = Buddhier()

print(base64.b64encode(bud.N.to_bytes(128, 'big')).decode())
print(base64.b64encode(bud.G.to_bytes(256, 'big')).decode())
print(base64.b64encode(bud.encrypt(int.from_bytes(FLAG, 'big')).to_bytes(256, 'big')).decode())

while True:

    try:
        offer = int(input())
        print(base64.b64encode(bud.barter(offer).to_bytes(256, 'big')).decode())

    except:
        break