#!/usr/bin/env python3
from pwn import *

r = remote("localhost", 1337)

with open("yeeeet.js", "r") as f:
	lines = f.readlines()

for line in lines:
	r.send(line)
r.sendline("EOF")

r.interactive()