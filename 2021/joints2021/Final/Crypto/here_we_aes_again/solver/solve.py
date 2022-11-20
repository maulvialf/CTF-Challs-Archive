from pwn import *
import json
from Crypto.Cipher import AES
from Crypto.Util import Counter
import struct
import os
import zlib

def crc(inp):
    return 0xffffffff ^ zlib.crc32(inp)

def gen_extra_code(json_str, key, aes_key):
    code = json_str.encode() + key
    code = code + struct.pack('<L', crc(code))
    aes_obj = AES.new(aes_key, AES.MODE_CTR, counter = Counter.new(128))
    return aes_obj.encrypt(code)

while True:
    r = remote("localhost", 5000)

    r.recvuntil("admin code : ")
    admin_code = r.recvline()[:-1].decode()

    r.recvuntil("regular user : ")
    extra_code = r.recvline()[:-1].decode()
    
    r.sendlineafter("> ", "1")

    r.sendlineafter("(in hex) : ", "0"*len(admin_code))
    r.recvline()
    first_tag = r.recvline()[:-1].decode().split("Tag : ")[1]

    r.sendlineafter("> ", "1")

    r.sendlineafter("(in hex) : ", "0"*(len(admin_code)-1) + "1")
    r.recvline()
    second_tag = r.recvline()[:-1].decode().split("Tag : ")[1]

    r.sendlineafter("> ", "1")

    r.sendlineafter("(in hex) : ", admin_code[:-2] + hex(int(admin_code[-2:],16)-1).replace("0x",""))
    fake_cipher = r.recvline()[:-1].decode().split("Code : ")[1]
    third_tag = r.recvline()[:-1].decode().split("Tag : ")[1]
    
    final_tag = hex(int(first_tag, 16) ^ int(second_tag, 16) ^ int(third_tag, 16)).replace("0x", "")
    final_cipher = fake_cipher[:-2] + hex(int(fake_cipher[-2:],16)-1).replace("0x","")

    r.sendlineafter("> ", "2")
    r.sendlineafter(": ", final_cipher)
    r.sendlineafter(": ", final_tag)

    result = r.recv()

    if b"identify" in result:
        mac_key = os.urandom(0x10)
        key_1 = os.urandom(16)
        key_2 = os.urandom(16)

        cipher_1 = gen_extra_code(json.dumps({'adm00n': 0}), key_1, key_2)
        cipher_2 = gen_extra_code(json.dumps({'adm00n': 1}), key_1, key_2)
        xor_cipher = xor(cipher_1, cipher_2)
        final = xor(xor_cipher, bytes.fromhex(extra_code))
        
        r.sendline(final.hex())

        print(r.recv())
        exit()

    r.close()