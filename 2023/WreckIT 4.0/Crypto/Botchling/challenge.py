from Crypto.Util.number import bytes_to_long
from secret import a, b, key, FLAG
from sage.all import *

p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000ffffffff
E = EllipticCurve(GF(p), (0, a, 0, b, 0))
G = E.gens()[0]

m = bytes_to_long(FLAG)
P = E.lift_x(Integer(m))
Q = P * key
x = int(pow(key + int(G[1]), m, E.order()))

assert (P * x)[0] == m
assert Q * (x+1) + G == G

print(f'G = {G}')
print(f'Q = {Q}')