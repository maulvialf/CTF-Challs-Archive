from Crypto.Util.number import *

m = bytes_to_long(b'REDACTED')
p = getPrime(1024)
q = getPrime(1024)
e = 3
n = p * q
c = pow(m, e, n)
print(f'n =', n)
print(f'e =', e)
print(f'c =', c)
