from deom import *

exec(open('output.txt').read())

def calc(a, b, c):
    s = float(a if b else -a)
    while True:
        s *= -c
        a += s
        if abs(s) < .0001:
            return int(a) + 1

def genPrime(x):
    p = calc(x, False, Fraction(11, 17))
    q = calc(x, True, Fraction(13, 19))
    return p, q

x = iroot(896 * n / 741, 2)[0]
print 'x =', x

_, q = genPrime(x)
p = n / q
print 'p =', p
print 'q =', q

d = inverse(65537, (p - 1) * (q - 1))
m = pow(c, d, n)
print n2s(m)
