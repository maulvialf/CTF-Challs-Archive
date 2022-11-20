c = 'J\x05\x06\x07\x1a\x07a\x03JN]\\Y\x08:0\x0112^l9\t=\r2Y_Z_\t8;Ub\x0c(\x12Tc6;<\x0b\\X\x00\t\x0b\tTN'
flag = 'J'
for i in range(1, len(c)):
    flag += chr(ord(c[i])^ord(flag[i-1]))

print(flag)