from Crypto.Util.number import *

m = bytes_to_long(b'REDACTED')
p = getPrime(256)
q = getPrime(256)
n = p*q
e = 65537
c = pow(m, e, n)
print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')
