from Crypto.Util.number import *

m = bytes_to_long(b'REDACTED')
p = getPrime(512)
q = getPrime(512)
e = 65537
n = p*q
c = pow(m, e, n)
print(f'n = ', n)
print(f'e = ', e)
print(f'c = ', c)
print(f'pplusq = ', p + q)
