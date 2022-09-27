import numpy as np

flag = 'REDACTED'

def encrypt(flag):
    np.random.seed(14145)
    peras = np.array([ord(c) for c in flag])
    manzanas = np.random.randint(1,8,(len(flag)))
    peras = np.multiply(peras,manzanas)
    b = [x for x in peras]
    z = [ord(x) for x in ''.join(['CERTUNLP'*15])]
    c = [b[i]^z[i] for i,j in enumerate(b)]
    c2 = ''.join(bin(x)[2:].zfill(8) for x in c)
    c3 = hex(int(c2,2))
    ofile=open("output.txt","w")
    ofile.write(c3)
    ofile.close()
    
encrypt(flag)

