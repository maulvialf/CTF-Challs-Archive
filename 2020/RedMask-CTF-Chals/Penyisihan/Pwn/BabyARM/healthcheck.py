#!/usr/bin/env python3
from pwn import *

HOST = "localhost"
PORT = 1337

if __name__ == '__main__':
	r = remote(HOST, PORT)
	try:
		assert(r.recvline(0, timeout=1) != b"")
		r.close()
	except:
		r.close()
		exit(1)
	exit(0)
