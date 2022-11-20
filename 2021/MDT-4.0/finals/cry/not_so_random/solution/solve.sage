#!/usr/bin/sage
from pwn import *
import string, time

from server import NotSoRandom

start = time.time()

# r = process('./server.py', level='warn')
r = remote('localhost', 30002, level='warn')
r.sendlineafter(b'> ', b'1')
r.sendlineafter(b'> ', b'1')
s2 = Integer(r.recvline(0).decode())

p = 0xffffffffffffffffffbf
P = GF(p)

abs = P(s2).nth_root(19, all=True)
pos = []

for ab in abs:
    mids = P(ab).nth_root(2, all=True)
    for mid in mids:
        seeds = P(mid).nth_root(2 * 5, all=True)
        pos += seeds

word = string.ascii_letters + string.digits
isPrintable = lambda x: all(i in word.encode() for i in x)

for po in pos:
    tmp = int.to_bytes(int(po), 10, 'big')
    if isPrintable(tmp[5:]):
        F1 = tmp[5:]
        seed = po
        break

nsr = NotSoRandom(Integer(seed))
nsr.next()
nsr.next()

a = Integer(nsr.next())
q = Integer(nsr.next())

r.sendlineafter(b'> ', b'2')
r.sendlineafter(b'guess: ', str(a).encode())
enc = Integer(r.recvline(0).decode())
r.close()

end = time.time()
print(f'{end-start} seconds')

assert enc % q == 0

F2 = int(enc // q)
F2 = int.to_bytes(F2, (F2.bit_length() + 7) // 8, 'big')
flag = F1 + F2
print(f'MDT4.0\x7b{flag.decode()}\x7d')
