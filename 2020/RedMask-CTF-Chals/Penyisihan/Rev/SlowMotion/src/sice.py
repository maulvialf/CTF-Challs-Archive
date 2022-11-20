#!/usr/bin/env python3
flag = b"redmask{0_125_byte_per_second__}"
key = 0x69

res = []
for c in flag:
    res.append(c ^ key)
    key ^= res[-1]
print(res)
