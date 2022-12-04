#!/usr/bin/env python3
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import os, random

FLAG = open("flag.txt", "rb").read()


def f1(msg, key):
    v1 = os.urandom(14)
    v2 = int.from_bytes(v1 + msg, "big")
    return pow(v2, key.e, key.n)


def f2(msg, key):
    v1 = int.from_bytes(SHA256.new(msg).digest(), "big")
    v2 = int.from_bytes(FLAG[:len(FLAG) // 2], "big")
    return theorem(noise(v1), v2, key)


def noise(x, nbit=14):
    return x ^ random.getrandbits(nbit)


def theorem(x, y, key):
    v1 = x * pow(key.q, -1, key.p) * key.q % key.n
    v2 = y * pow(key.p, -1, key.q) * key.p % key.n
    return (v1 + v2) % key.n


def user_input(s=""):
    inp = input(s).strip()
    assert len(inp) < 2048
    return inp


def main():
    print("Menu:\n(1) Use function #1\n(2) Use function #2\n(3) Exit")
    key = RSA.generate(1536)
    for _ in range(3):
        opt = int(user_input("\n> "))

        if opt == 1:
            msg = user_input("[+] Message: ").encode()
            msg = FLAG[len(FLAG) // 2:] if msg == b"FLAG" else msg
            print("[+] Result:", f1(msg, key))

        elif opt == 2:
            msg = user_input("[+] Message: ").encode()
            msg = FLAG[len(FLAG) // 2:] if msg == b"FLAG" else msg
            print("[+] Result:", f2(msg, key))

        elif opt == 3:
            print("[+] Bye!")
            break

        else:
            print("[-] ?")


if __name__ == "__main__":
    main()
