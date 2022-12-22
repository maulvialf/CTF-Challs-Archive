#!/usr/bin/env python3
from functools import reduce
import gmpy2, libnum, random

FLAG = open("flag.txt", "rb").read()
assert len(FLAG) == 50


def gen_kxn():
    k = random.getrandbits(200)
    while True:
        x = random.getrandbits(134)
        box = [x := int(gmpy2.next_prime(13 * x - 37)) for _ in range(10)]
        n = reduce(lambda x, y: x * y, box)
        if n.bit_length() == 1536:
            return [k, x, n]


def gen_num(idx, k, x, n):
    b = int(libnum.s2b(FLAG)[20 * idx:20 * idx + 20], 2)
    return hex(pow(x, k ^ (b << (20 * idx)), n))


def main():
    k, x, n = gen_kxn()
    list(map(print, [gen_num(idx, k, x, n) for idx in range(20)]))


if __name__ == "__main__":
    main()
