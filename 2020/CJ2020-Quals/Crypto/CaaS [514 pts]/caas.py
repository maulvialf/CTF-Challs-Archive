from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from CTFInternal import key, iv
import sys


class Service:
    def __init__(self):
        self.aes_obj = AES.new(key, AES.MODE_OFB, iv)

    def encrypt(self, s):
        padding_len = 16 - (len(s) & 0xf)
        plain_text= (s + chr(padding_len) * padding_len).encode("utf-8")
        cipher_bytes = self.aes_obj.encrypt(plain_text)
        encoded_cipher_bytes = b64encode(cipher_bytes).decode('utf-8')
        return encoded_cipher_bytes

    def user_interaction(self):
        print('Insert a text to encrypt:')
        sys.stdout.flush()
        plain_text = input()
        encrypted = self.encrypt(plain_text)
        print('\nResult:')
        print(encrypted)
        sys.stdout.flush()

service = Service()
service.user_interaction()
