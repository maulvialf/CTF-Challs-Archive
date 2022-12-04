from random import randint
from hashlib import sha256
from Crypto.Util.number import bytes_to_long
from ecdsa import ellipticcurve


class FaustianContract:

    def __init__(self):

        p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
        a = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc
        b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b

        Gx = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
        Gy = 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
        self.n = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551

        self.E = ellipticcurve.CurveFp(p, a, b, 1)

        self.G = ellipticcurve.PointJacobi(self.E, Gx, Gy, 1, self.n)
        self.x = randint(1, self.n - 1)
        self.y = randint(1, self.n - 1)
        self.Q = self.G * self.x

    def sign(self, m):
        h = bytes_to_long(sha256(m).digest())
        k = self.x + h
        R = k * self.G
        S = self.y * self.G
        t = ((R.x() * self.y) + (S.x() * k) + (h * self.x)) % self.n

        return (int(R.x()), int(R.y())), (int(S.x()), int(S.y())), int(t)

    def verify(self, m, R, S, t):

        if t < 1 or t > self.n:
            return False

        if not self.E.contains_point(R[0], R[1]):
            return False

        if not self.E.contains_point(S[0], S[1]):
            return False

        h = bytes_to_long(sha256(m).digest())

        R = ellipticcurve.PointJacobi(self.E, R[0], R[1], 1, self.n)
        S = ellipticcurve.PointJacobi(self.E, S[0], S[1], 1, self.n)
        return t * self.G == (self.Q * h) + (R * S.x()) + (S * R.x())


if __name__ == "__main__":

    FLAG = open('flag.txt', 'r').read()

    try:
        contract = FaustianContract()
        pacts = [
            "Memento Mori",
            "Mors Vincit Omnia",
            "Vita Vanitas"
        ]

        print("Welcome to the Faustian Bargain...")
        print("What do you want to trade??")
        print()

        print("My agreement:")
        print("===================")
        for i in range(2):
            R, S, t = contract.sign(pacts[i].encode())
            print("R:", R)
            print("S:", S)
            print("t:", t)
            print()

        print("Your agreement:")
        print("===================")
        Rx = int(input("Rx: "))
        Ry = int(input("Ry: "))
        Sx = int(input("Sx: "))
        Sy = int(input("Sy: "))
        t = int(input("t: "))

        if contract.verify(pacts[2].encode(), (Rx, Ry), (Sx, Sy), t):
            print("GOOD agreement!")
            print("I receive your meaningless soul")
            print("You receive my flag")
            print(FLAG)
        else:
            print("BAD agreement!")

    except Exception as e:
        print("Something weird happen")
