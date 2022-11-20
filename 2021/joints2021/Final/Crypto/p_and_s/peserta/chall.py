#!/usr/bin/env python3
import random
import sys

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


flag = open("flag.txt").read().strip()
secret = [random.randint(3,225)]*9
RANDOM_BOX = []

try:
    ind_secret = int(input("Input Index for Secret : "))
    assert ind_secret in range(len(flag))
except:
    print("Invalid Index !")
    sys.exit(1)


for i in range(len(flag)):
    temp = [random.randint(0,255) for x in range(555)]
    if i == ind_secret:
        temp = temp[:-9] + secret
    RANDOM_BOX.append(temp)


print('''
Choose Option
1.)Get encrypted flag
2.)Encrypt a string
3.)Check flag
''')

while True:
    choice = input(">>> ").lower()
    
    if choice == "1" or choice == "2":
        try:
            amount = int(input("How Many Times ? : "))
            if amount > 5000 or amount < 1:
                sys.exit(1)
        except:
            print("Something Error !")
            sys.exit(1)
        
        arr_cipher = []
        var = flag
        
        if choice == "2":
            var = input("Enter Plaintext : ")
            if len(var) != len(flag):
                print("The length of the plaintext must be same with the flag")
                break

        for n in range(amount):
            cipher = ""
            
            for indeks in range(len(var)):
                cipher += chr(ord(var[indeks]) ^ random.choice(RANDOM_BOX[indeks]))
            
            arr_cipher.append(cipher.encode("latin-1").hex())
        
        print(f"Cipher : {arr_cipher}")
    
    elif choice == "3":
        flag_input = input("Masukan string flag : ")
        
        if flag_input == flag:
            print(f"Correct,your flag : {flag}")
        else:
            print("WRONG !")
        break
    
    else:
        print("Invalid Choice !")
        break
