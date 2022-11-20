#!/usr/bin/python
from Crypto.Hash import SHA256
from pwn import *

EMPTY = SHA256.new('').hexdigest()

to_blocks = lambda x: [x[i:i+16] for i in range(0, len(x), 16)]

def dekrip(x):
    r.sendlineafter('> ', '3')
    r.sendlineafter('ct: ', x.encode('hex'))
    r.recvuntil('SHA256(Decrypt(ct)): ')
    return r.recvline(0)

def solve_blocks(enc):
    arr = []
    for i in range(256):
        tmp = list(enc[-2])
        tmp[-1] = chr(i)
        tmp = ''.join(tmp)

        test = enc
        test[-2] = tmp
        test = ''.join(test)

        res = dekrip(test)
        if res != EMPTY:
            arr.append(res)

    res = ''
    found = True
    while found:
        found = False
        for i in range(256):
            test = res + chr(i)
            if SHA256.new(test).hexdigest() in arr:
                res += chr(i)
                print repr(res)
                found = True
                break

        if len(res) == 16:
            break

    return res

flag = ''

for i in range(3):
    # r = process('./server.py')
    r = remote('localhost', 30001)
    r.sendlineafter('> ', '1')
    r.recvuntil('Encrypt(FLAG): ')

    enc = r.recvline(0)
    enc = to_blocks(enc.decode('hex'))

    enc_blocks = [enc]
    enc_blocks += [[enc[1], enc[2], enc[2], enc[3]]]
    enc_blocks += [[enc[2], enc[3], enc[2], enc[3]]]

    flag += solve_blocks(enc_blocks[i])
    r.close()

print repr(flag)
