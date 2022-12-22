from random import randint, choice
from hashlib import sha256
from Crypto.Util.number import bytes_to_long, inverse
from ecdsa import ellipticcurve
import pacts


class MephistoContract:

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
        self.Q = self.G * self.x

    def sign(self, m):
        h = bytes_to_long(sha256(m).digest())
        k = self.x + h
        l = self.x ^ h
        R = k * self.G
        S = l * self.G
        t = ((R.x() * l) + (S.x() * k) + (h * self.x)) % self.n

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

    opening = "Ego, {}, volo facere pactum cum te, Mephistopheles. Pro mea anima, quae tu mihi dabis desiderium, et pro tua promissione ad me dedere beneficium, ego accipio tecum istud pactum et promitto ad tuas condiciones adimplere. Si ego fallo ad tuas condiciones, tu habes potestatem ad meam animam capere. Ita pactum sit."

    contract = MephistoContract()

    name = input('Enter your name: ')

    print(opening.format(name))
    print()
    is_agree = input('Do you accept (y/n) ? ')

    if is_agree == 'y':
        print('You\'ve chosen to abandon your humanity I see')
        print()
        print("My offering:")
        print("===================")
        for _ in range(13):
            R, S, t = contract.sign(choice(pacts.pacts).encode())
            print("R:", R)
            print("S:", S)
            print("t:", t)
            print()
            more = input("Need more (y/n) ? ")
            if more == 'n':
                break

        print()
        print("Your offering:")
        print("===================")
        Rx = int(input("Rx: "))
        Ry = int(input("Ry: "))
        Sx = int(input("Sx: "))
        Sy = int(input("Sy: "))
        t = int(input("t: "))

        if contract.verify(b'Daemonum Superbia!', (Rx, Ry), (Sx, Sy), t):
            print(FLAG)
        else:
            print("BAD agreement!")
    else:
        print('Wise choice, human!')
