#!/usr/bin/python

import secret
import random
from Crypto.Util.number import getPrime

import os
import sys

PRIME = [227, 229, 233, 239, 241, 251]
random.seed(os.urandom)
random.shuffle(PRIME)

class PRNG:
    a = secret.a
    c = secret.c
    m = secret.m

    def __init__(self, seed):
        self.state = seed

    def generate(self):
        self.state = self.state * self.a % self.m + self.c % self.m
        self.state = self.state % self.m
        return self.state

def main():
    seed = 1337
    gen = PRNG(seed)
    enc = []
    num = []
    hint1 = []
    flag = secret.flag

    for i in range(len(flag)):
        tmp = gen.generate()
        num.append(tmp)
        if(i < 6):
            prime = PRIME.pop()
            print(prime)
            tmp1 = tmp
            tmp = tmp ^ prime
            tmp1 = tmp1 - prime
            hint1.append(tmp1)
        res = ord(flag[i]) ^ tmp
        enc.append(res)

    print("enc: ",enc)
    print("hint1: ",hint1)

if __name__ == '__main__':
    main()

# ('enc: ', [142480696398, 438972531026L, 193822069683L, 153738699609L, 522944679201L, 103858046402L, 409824720605L, 198554268540L, 348493614739L, 488958573233L, 38043882350L, 134688189824L, 607629205198L, 71957319932L, 325998949710L, 82904829550L, 304318025700L, 592453289291L, 330191952240L, 92418422406L, 475183248833L, 381745574390L, 366232332191L, 51709560611L, 329628356407L, 451733888491L, 448890570242L, 13655771114L, 512318117959L, 355619685020L, 431700304607L, 657184352851L, 687484633817L, 222947793440L, 118488991997L])
# ('hint1: ', [142480696324, 438972530923L, 193822069306L, 153738699529L, 522944679058L, 103858046102L])