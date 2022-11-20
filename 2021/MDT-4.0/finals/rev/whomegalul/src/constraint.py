a = [3077294402, 1551376434, 26199182, 53009198]
# hostname = "eLit3_uname_1337"
data = []
for i in range(4):
    for j in range(4):
        if i != j:
            data.append(a[i] + a[j])
print data