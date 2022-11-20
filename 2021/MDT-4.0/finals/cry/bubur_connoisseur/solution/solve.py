#!/usr/bin/python
from pwn import *

# r = process('./server.py')
r = remote('localhost', 30001)

def tulis(payload):
    r.sendlineafter('> ', '1')
    r.sendlineafter('Nama: ', payload)
    r.sendlineafter('Sekte (diaduk/tidak diaduk): ', 'diaduk')
    r.sendlineafter('Rating (1-5): ', '5')
    r.recvuntil('Kupon: ')
    return r.recvline(0)

def redeem(kupon):
    r.sendlineafter('> ', '2')
    r.sendlineafter('Kupon: ', kupon)
    return r.recvline(0)

to_32 = lambda x: [x[i:i+32] for i in range(0, len(x), 32)]

k1 = tulis('aaaaaadiblender')
k2 = tulis('aaaaaaaaa')
k3 = tulis('aaaaaaaaaaaaa')

c1 = to_32(k1)
c2 = to_32(k2)
c3 = to_32(k3)

payload  = ''
payload += c2[0]
payload += c2[1]
payload += c1[1]
payload += c3[2]
payload += c3[3]
payload += c3[5]
payload += c3[6]

bubur = redeem(payload)
print bubur
