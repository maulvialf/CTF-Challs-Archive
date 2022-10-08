from Crypto.Util.number import bytes_to_long
from secret import p, q, r, s, d, FLAG

m = bytes_to_long(FLAG)

n = p*q*r*s

A = pow(2, d, n)
s = pow(A, d, n)
A = pow(A, 2, n)

c = m ^ s

print(f'n = {n}')
print(f'A = {A}')
print(f'c = {c}')