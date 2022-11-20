import math
from sympy import gcd
import functools
from sympy import isprime

reduce = functools.reduce

values = [142480696398, 438972531026L, 193822069683L, 153738699609L, 522944679201L, 103858046402L, 409824720605L, 198554268540L, 348493614739L, 488958573233L, 38043882350L, 134688189824L, 607629205198L, 71957319932L, 325998949710L, 82904829550L, 304318025700L, 592453289291L, 330191952240L, 92418422406L, 475183248833L, 381745574390L, 366232332191L, 51709560611L, 329628356407L, 451733888491L, 448890570242L, 13655771114L, 512318117959L, 355619685020L, 431700304607L, 657184352851L, 687484633817L, 222947793440L, 118488991997L]
hint =  [142480696324, 438972530923L, 193822069306L, 153738699529L, 522944679058L, 103858046102L]

class Random():	
    n = 0
    m = 0
    c = 0

    print("n =" + str(n))
    print("m =" + str(m))
    print("c =" + str(c))
    
    def __init__(self, s):
		self.state = s
    
    def next(self):
		self.state = (self.m * self.state + self.c) % self.n
		return self.state

def encrypt(message, r):
	for i in range(100):
		r.next()

	encrypted = []
	for c in message:
		encrypted.append(ord(c) ^ r.next())
	return encrypted

def crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(gcd, zeroes))
    return crack_unknown_multiplier(states, modulus)

def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * modinv(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)

def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def decrypt(message, r):
    decrypted = ""
    for c in message:
        char = chr((c ^ int(r.next())))
        decrypted+=char
    return decrypted

prime = [227, 229, 233, 239, 241, 251]

val = []
target = "JOINST"

for i in range(6):
    for p in prime:
        tmp = ord(target[i]) ^ (p + hint[i]) ^ p
        if (tmp == values[i]):
            val.append(p + hint[i])
            break

seed = 1337
r = Random(seed)
r.n, r.m, r.c =  crack_unknown_modulus(val)
print r.n
print r.m
print r.c

print decrypt(values,r)