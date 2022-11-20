#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

FLAG = open('flag.txt', 'rb').read()

class Unpredictable:
    def __init__(self):
        self.key = AES.get_random_bytes(AES.block_size)

    def encrypt(self, pt):
        iv = AES.get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(self.pad(pt))

    def decrypt(self, ct):
        iv = ct[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(ct[16:]))

    def pad(self, msg):
        l = 16 - (len(msg) % 16)
        return msg + bytes([l] * l)

    def unpad(self, msg):
        l = msg[-1]
        return msg[:-l]

def user_input(s):
    inp = input(s).strip()
    assert len(inp) < 1024
    return inp

def banner():
    print('-' * 30)
    print('1. Encrypt(FLAG)')
    print('2. pt -> Encrypt(pt)')
    print('3. ct -> SHA256(Decrypt(ct))')
    print('4. pt -> SHA256(pt)')
    print('-' * 30)

def main():
    aes = Unpredictable()
    banner()
    for _ in range(300):
        opt = user_input('> ')
        if opt == '1':
            enc_flag = aes.encrypt(FLAG).hex()
            print('| Encrypt(FLAG): ' + enc_flag)

        elif opt == '2':
            pt = user_input('| pt: ').encode()
            ct = aes.encrypt(pt).hex()
            print('| Encrypt(pt): ' + ct)

        elif opt == '3':
            try:
                ct = bytes.fromhex(user_input('| ct: '))
                pt = aes.decrypt(ct)
                hh = SHA256.new(pt).hexdigest()
                print('| SHA256(Decrypt(ct)): ' + hh)
            except:
                print('| Bad ct...')

        elif opt == '4':
            pt = user_input('| pt: ').encode()
            hh = SHA256.new(pt).hexdigest()
            print('| SHA256(pt): ' + hh)

        else:
            break

        print('-' * 30)

if __name__ == '__main__':
    main()
