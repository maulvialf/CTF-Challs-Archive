#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from gmpy2 import digits

key = RSA.import_key(open('key.pem').read())
msg = int(digits(int.from_bytes(open('flag.txt', 'rb').read(), 'little'), 8))
enc = int.to_bytes(pow(msg, key.e, key.n), 128, 'little')
open('flag.enc', 'wb').write(enc)
