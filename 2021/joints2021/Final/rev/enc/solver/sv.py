def dec(x):
    a = ((x[0] << 2) & 0xff) | ((x[1] >> 4) & 3)
    b = ((x[1] << 4) & 0xff) | ((x[2] >> 2) & 15)
    c = ((x[2] << 6) & 0xff) | (x[3] & 0x3f)
    fl = chr(a) + chr(b) + chr(c)
    return fl

T = "o5Rkw4VEt1rxYiT/vB2lg6XfjQHndANGb3+JmFc8MUSPOKZ0qC7DpaLzsue9WyIh"
# enc_fl = "BBsafGUoUV4ZAjABDj0CMAQNPgEzBRIzESoLFDEUHCg1fUZG"
enc_fl="j8bE/VKcjcULkCm6jmdYxl4rtbidR2vNd+CdRFuawXuAHodliRQP"
#enc_fl="Hx8fcG9w"
enc_fl = [list(enc_fl[i:i+4]) for i in range(0, len(enc_fl), 4)]
for i in range(len(enc_fl)):
    for j in range(4):
        x = enc_fl[i][j]
        enc_fl[i][j] = T.index(x)

for k in range(100):
    for p in range(4):
        enc_fl[-1][p]^=enc_fl[0][p]
    for i in range(len(enc_fl)-2, -1, -1):
        for j in range(4):
            enc_fl[i][j] ^= enc_fl[i+1][j]


flag = ""
for i in range(len(enc_fl)):
    flag += dec(enc_fl[i])

print(flag)
