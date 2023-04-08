from Crypto.Util.number import *
import random
from sympy import *

FLAG = b"REDACTED"
def prime_generation():
	p = getPrime(512)
	q = nextprime(p)
	while p%4 != 3 or q%4 !=3:
		p = getPrime(512)
		q = nextprime(p)
	return p, q

def encryption(m, n):
	return (pow(pow(m,2,n)*(m*m),4,n))%n

p, q = prime_generation()
n = p*q
m = bytes_to_long(FLAG)

ct = encryption(m, n)

file = open('hasil.txt', 'w')
file.write(f"n = {n}\nct = {ct}")
