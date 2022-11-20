#!/usr/bin/env python3
import random, re, signal, sys

class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

FLAG = open('flag.txt', 'rb').read()
FLAG = re.findall(rb'MDT4.0{(\w+)}', FLAG)[0]
F1 = int.from_bytes(FLAG[:5], 'big')
F2 = int.from_bytes(FLAG[5:], 'big')

class NotSoRandom:
    def __init__(self, seed):
        self.p = 0xffffffffffffffffffbf
        self.a, self.b = seed, seed

    def next(self):
        self.a, self.b = pow(self.b, 2, self.p), pow(self.a, 5, self.p)
        return pow(self.a * self.b, 19, self.p)

def user_input(s):
    inp = input(s).strip()
    assert len(inp) < 1024
    return inp

def main():
    seed = (random.getrandbits(40) << 40) | F1
    nsr = NotSoRandom(seed)
    for _ in range(3):
        opt = user_input('> ')
        if opt == '1':
            print(nsr.next())
        elif opt == '2':
            guess = int(user_input('guess: '))
            if guess == nsr.next():
                print(F2 * nsr.next())
            else:
                print('try harder...')
        else:
            break

if __name__ == '__main__':
    signal.alarm(40)
    main()
