import gensafeprime
from gmpy import *
from Crypto.Util.number import *

bits = 3
a = gensafeprime.generate(2 * bits)
a = 10
while True:
    g = getRandomRange(2, a)
    if pow(g, 2, a) != 1 and pow(g, a // 2, a) != 1:
        break

print (g)