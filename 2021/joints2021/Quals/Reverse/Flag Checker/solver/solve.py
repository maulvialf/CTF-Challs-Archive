charset = 'qwertyuiopasdfghjklzxcvbnm0123456789_'
c = '82174ed8dbebcee3bdd38bd65e44f5c6490d'


cc = []
for i in range(int(len(c)/6)):
    cc.append(int(c[i*6:i*6+6], 16))

res = {}
for i in charset:
    for j in charset:
        for k in charset:
            for l in charset:
                tmp = ord(i) ^ ord(j)
                tmp *= ord(k)
                tmp += ord(l)
                tmp ^= (ord(i)**3)
                tmp *= ord(i)
                tmp -= ord(k)
                tmp %= 0xffffff
                res[i,j,k,l] = tmp


for i in cc:
    ans = []
    for j in res:
        if(res[j] == i):
            ans.append(''.join(j))
    print(ans)