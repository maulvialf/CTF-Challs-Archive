from Crypto.Util.number import *
import random
from secret import flag

def get_prime():
    i = int.from_bytes(str(random.getrandbits(512)).encode(), byteorder='big')
    if isPrime(i):
        return i
    else:
        return get_prime()

p = get_prime()
q = get_prime()
n = p * q
e = 1337
m = bytes_to_long(flag)
c = pow(m, e, n)

print(f"n = {n}\ne = {e}\nc = {c}")