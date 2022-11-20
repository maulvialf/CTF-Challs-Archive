
from z3 import *
from zlib import crc32
import string
import hashlib

s = Solver()
v1 = [BitVec(i, 32) for i in range(4)]

out = [4628670836, 3103493584, 3130303600, 4628670836, 1577575616, 1604385632, 3103493584, 1577575616, 79208380, 3130303600, 1604385632, 79208380]
# ================================
counter = 0

for i in range(4):
    for j in range(4):
        if i != j:
            s.add(v1[i] + v1[j] == out[counter])
            counter += 1

# ================================

if s.check() == sat:
    model = s.model()
    res = [(model[x].as_long()) for x in v1]
    print res

    chars = string.uppercase + string.lowercase + string.digits + '_'
    big_dic = {}
    
    for i in chars:
        for j in chars:
            for k in chars:
                for l in chars:
                    big_dic[crc32(i+j+k+l) & 0xffffffff] = i+j+k+l
    
    print "MDT4.0{" + hashlib.sha1("".join([big_dic[i] for i in res])).hexdigest() + "}"