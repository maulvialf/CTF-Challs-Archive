
cipher = raw_input('Cipher :')
blocks = []
for i in range(0,len(cipher),32):
    print(cipher[i:i+32])