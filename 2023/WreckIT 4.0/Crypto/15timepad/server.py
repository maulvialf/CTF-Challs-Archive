#!/usr/bin/env python3
from base64 import urlsafe_b64encode as e
from hashlib import sha384 as h
import random
import re

FLAG = re.findall(r"^WRECKIT40{(\w+)}$", open("flag.txt").read())[0]
HALF = 18
assert len(FLAG) == 2 * HALF

x = lambda a, b: bytes([x ^ y for x, y in zip(a, b)])


class Challenge:
    def __init__(self):
        self.m = pow(2, 8 * HALF)
        self.a = random.randrange(2, self.m - 2, 2)
        self.b = random.randrange(self.a, self.m)
        self.x = int.from_bytes(FLAG[HALF:].encode())

    def getrandnum(self):
        self.x = (self.a * self.x - self.b) % self.m
        return self.x

    def getrandchars(self):
        return hex(self.getrandnum())[2:]

    def encrypt(self, f: str):
        g = str(random.randint(pow(10, len(f) - 1), pow(10, len(f)) - 1)).encode()
        return e(h(f.encode()).digest() + x(e(x(f.encode(), g)), e(g))).decode()


def main():
    chall = Challenge()
    for _ in range(5):
        m = chall.getrandchars()
        print("<< " + chall.encrypt(m))
        if input(">> ").strip() != m:
            print("Wrong!")
            exit()

    print("Congrats! Here are the prizes for you:")
    print("++ " + e(FLAG[:HALF].encode()).decode())
    print("++ " + h(FLAG.encode()).hexdigest())


if __name__ == "__main__":
    main()
