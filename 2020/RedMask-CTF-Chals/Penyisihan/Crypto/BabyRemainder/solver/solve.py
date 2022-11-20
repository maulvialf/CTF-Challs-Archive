from deom import *
import itertools

output = open('../peserta/output.txt').read()
output = output.replace('[*] ', '')
output = output.replace(': ', '=')
exec(output)

C = c
N = n
print 'Flag bit-length: %d' % (int(N.bit_length() / 3.0))

def prevPrime(x):
    y = x | 1
    while not isPrime(y) or x == y:
        y -= 2
    return y

def prod(ns):
    bign = 1
    for n in ns:
        bign *= n
    return bign

rem_blocks = []
prime = prevPrime(x & 0xFFFFFF)
x >>= 24
while x:
    rem_blocks.append(x & 0xFFFFFF)
    x >>= 24
rem_blocks = rem_blocks

mod_blocks = [prime]
while len(rem_blocks) != len(mod_blocks):
    prime = prevPrime(prime)
    mod_blocks.append(prime)
mod_blocks = mod_blocks

for i in range(16):
    tmp = '}' + (chr(i + 1) * (i + 1))
    v0 = s2n(tmp)
    v1 = 256 ** len(tmp)
    cs = rem_blocks + [v0]
    ns = mod_blocks + [v1]
    res = solve_crt(cs, ns)
    prodn = prod(ns)
    for k in range(1024):
        tes = k*prodn + res
        if pow(tes, 65537, N) == C:
            print i, k, unpad(n2s(tes), 16)
            break
