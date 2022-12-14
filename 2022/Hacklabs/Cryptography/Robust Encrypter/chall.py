from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
from base64 import b64encode, b64decode
import random
from secret import flag

class Cipher:
    def __init__(self):
        self.g = 10
        self.p = 855098176053225973412431085960229957742579395452812393691307482513933863589834014555492084425723928938458815455293344705952604659276623264708067070331
        self.x = random.randint(2, self.p-1)
        self.y = pow(self.g,self.x,self.p)

    def encrypt(self, m: int) -> str:
        k = random.randint(2, self.p-1)
        c1 = pow(self.g, k, self.p)
        s = pow(self.y,k,self.p)
        c2 = (s * m) % self.p
        c1 = b64encode(long_to_bytes(c1)).decode()
        c2 = b64encode(long_to_bytes(c2)).decode()
        return c1 + "." + c2

    def decrypt(self, ct: str) -> str:
        c1, c2 = ct.split(".")
        c1 = bytes_to_long(b64decode(c1))
        c2 = bytes_to_long(b64decode(c2))
        s = inverse(pow(c1,self.x,self.p), self.p)
        m = (c2 * s) % self.p
        return long_to_bytes(m)

cipher = Cipher()

print(f"p = {cipher.p}")
print(f"g = {cipher.g}")
print(f"y = {cipher.y}")
flag = cipher.encrypt(bytes_to_long(flag.encode()))
print(f"Flag = {flag}")
print("")
 
for i in range(1):
    print("1. Encrypt")
    print("2. Decrypt")
    print("")

    try:
        option = int(input("Enter Your option: "))
        if option == 1:
            msg = input("Enter Your Message: ").encode()
            ct = cipher.encrypt(bytes_to_long(msg))
            print(f"Ciphertext = {ct}")

        if option == 2:
            msg = input("Enter Your Ciphertext (in base64 encoded): ")
            if msg == flag:
                raise Exception(":(((")
            pt = cipher.decrypt(msg)
            print(f"Plaintext = {b64encode(pt).decode()}")

    except Exception as e:
        print("Invalid input")
        exit(1)
