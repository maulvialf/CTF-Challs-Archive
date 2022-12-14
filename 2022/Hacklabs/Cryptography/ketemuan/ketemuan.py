from Crypto.Cipher import AES
import random
from Crypto.Util.Padding import pad


first_key = b""
second_key = b""
FLAG = b"REDACTED"

def generateKey():
	global first_key, second_key
	first_key = (str(random.randint(0, 999999)).zfill(6)*4)[:16].encode()
	second_key = (str(random.randint(0, 999999)).zfill(6)*4)[:16].encode()

def encrypt(plaintext, a, b):
	cipher = AES.new(a, mode=AES.MODE_ECB)
	ct = cipher.encrypt(pad(plaintext, 16))
	cipher = AES.new(b, mode=AES.MODE_ECB)
	ct = cipher.encrypt(ct)
	return ct.hex()

def main():
	generateKey()
	print("flag lu:", encrypt(FLAG, first_key, second_key))
	while True:
		print("encrypt apah:")
		plain = input(">> ")
		print("hasil:", encrypt(plain.encode(), first_key, second_key))

if __name__ == '__main__':
	main()