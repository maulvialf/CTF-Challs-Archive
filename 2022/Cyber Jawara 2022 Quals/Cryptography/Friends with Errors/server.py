#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
import os

FLAG = open("flag.txt").read()


def encrypt(msg: bytes, key):
    m = bytes_to_long(msg)
    if m >= key.n:
        print(f"[-] Error: {hex(m)} supposed to be less than key.n")
        exit()

    c = pow(m, key.e, key.n)
    return long_to_bytes(c)


def test_decryption(msg: bytes, enc: bytes, key):
    m = bytes_to_long(msg)
    c = bytes_to_long(enc)
    if m >= key.n or c >= key.n:
        print(f"[-] Error: {hex(m)} and {hex(c)} supposed to be less than key.n")
        exit()

    phi = (key.p - 1) * (key.q - 1)
    d = pow(key.e, -1, phi)
    z = (d - key.d) % pow(2, key.d.bit_length() // 2)
    if z:
        print(f"[-] Error: {hex(z)} supposed to be zero")
        exit()

    print("[+] Good message" if m == pow(c, d, key.n) else "[-] Bad message")


def user_input(s=""):
    inp = input(s).strip()
    assert len(inp) < 2048
    return inp


def main():
    print("Menu:\n(1) Encrypt message\n(2) Test Decryption\n(3) Encrypt flag\n(4) Exit")
    key = RSA.generate(1536)
    for _ in range(4):
        opt = int(user_input("\n> "))

        if opt == 1:
            msg = user_input("[+] Message: ").encode()
            print("[+] Encrypted message:", encrypt(msg, key).hex())

        elif opt == 2:
            msg = user_input("[+] Message: ").encode()
            enc = bytes.fromhex(user_input("[+] Encrypted message: "))
            test_decryption(msg, enc, key)

        elif opt == 3:
            pad = os.urandom(16)
            print("[+] Encrypted flag:", encrypt(pad + FLAG.encode(), key).hex())

        elif opt == 4:
            print("[+] Bye!")
            break

        else:
            print("[-] ?")


if __name__ == "__main__":
    main()
