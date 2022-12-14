from Crypto.Util.number import *
import random
from sympy import *

FLAG = b"hacklabs{REDACTED}"
def generate_prime():
	p = getPrime(512)
	q = nextprime(p)
	while p%4 != 3 or q%4 !=3:
		p = getPrime(512)
		q = nextprime(p)
	return p, q

def encrypt(m, n):
	return pow(m, 256, n)

p, q = generate_prime()
n = p*q
m = bytes_to_long(FLAG)

ct = encrypt(m, n)

file = open('out.txt', 'w')
file.write(f"n = {n}\nct = {ct}")