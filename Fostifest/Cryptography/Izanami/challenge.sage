from Crypto.Util.number import *
from secret import p, q, r, a, b, d, G, FLAG

m = bytes_to_long(FLAG)

n = p*q*r

E = EllipticCurve(Zmod(n), [a, b])

G = E(G)
P = d * G

c = m ^^ d

print(f'n = {n}')
print(f'G = {G}')
print(f'P = {P}')
print(f'c = {c}')