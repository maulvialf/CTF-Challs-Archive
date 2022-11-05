#!/usr/bin/env python3

import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from message import flag,m1,m2

KEY = get_random_bytes(16)
NONCE = get_random_bytes(16)

def aes_gcm_encrypt(plaintext):
    cipher = AES.new(KEY, AES.MODE_GCM, nonce=NONCE)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return ciphertext.hex(), tag.hex()

def aes_gcm_decrypt(ciphertext, tag):
    cipher = AES.new(KEY, AES.MODE_GCM, nonce=NONCE)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext

if __name__ == '__main__':
    print("Hey i captured your crush message but i can't decode the last message i've made you the decryption function next step is yours, our business is over\n")
    
    options = '''
1. Decrypt message
2. Quit
'''
    def decrypt():
        user_input = bytearray.fromhex(input('Encrypted text : '))
        tag = bytearray.fromhex(input('Tag : '))
        try:
            output = aes_gcm_decrypt(user_input, tag)
        except ValueError:
            print("Failed to decrypt")
            return
        print(f"\nThe message is : {output.decode('latin1')}")

    def quit():
        sys.exit()

    menu = {
        '1' : decrypt,
        '2' : quit,
    }

    print(f'Message 1 : {aes_gcm_encrypt(m1)}')
    print(f'Message 1 : {aes_gcm_encrypt(m2)}')
    print(f'Secret 1 : {aes_gcm_encrypt(flag)[0]}')

    i = 0

    while i < 10:
        print(options)
        choice = input('Input : ')
        if choice not in menu.keys():
            print("Not a valid menu....")
            sys.exit()
        menu[choice]()
        i += 1