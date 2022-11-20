from PIL import Image
from zlib import *
from z3 import *

import re
import struct

# Regex rule
idat = re.compile(rb'.{4}IDAT(.*?).{8}IEND', re.S)
png = re.compile(rb'.PNG.*?IEND....', re.S)

def pack(length):
    return struct.pack('!I', eval(f'{length}'))

def calc_crc(data):
    checksum = crc32(data) % (1<<32)
    return struct.pack('>I', checksum)

def calc_size(length):
    s = Solver()
    w = Int('w')
    h = Int('h')

    s.add(h + 3*h*w == length)
    s.add(w >= 20, w <= 30)
    s.add(h >= 20, h <= 30)

    dim = []
    while s.check() == sat:
        width = s.model()[w].as_long()
        height = s.model()[h].as_long()
        
        dim.append((width, height))
        break

    if not dim:
        s.reset()
        s.add(h + 3*h*w == length)
        s.add(w >= 20, w <= 60)
        s.add(h >= 20, h <= 60)

        while s.check() == sat:
            width = s.model()[w].as_long()
            height = s.model()[h].as_long()

            dim.append((width, height))
            s.add(Or(h != s.model()[h], w != s.model()[w]))

            if len(dim) > 3:
                break

    return dim

def find_ptrn(imgs):
    h = [_.size[1] for _ in imgs]

    for i in range(1, len(h)):
        g1 = h[:i]
        g2 = h[i:i*2]

        if g1 == g2:
            return g1


raw = open('code.png', 'rb').read()
img = png.findall(raw)
dat = idat.findall(raw)

imgs = []
for im, data in zip(img, dat):
    raster_data = decompress(data)
    size = calc_size(len(raster_data))

    head = im[:16]
    partial_data = im[24:29]
    trailer_data = im[33:]

    for s in size:
        size_data = pack(s[0]) + pack(s[1])
        data = im[12:16] + size_data + partial_data
        chunk_crc = calc_crc(data)

        with open('tmp.png', 'wb') as handle:
            content = (
                head
              + size_data 
              + partial_data
              + chunk_crc
              + trailer_data
            )

            handle.write(content)

        try:
            image = Image.open('tmp.png')
            image.tobytes()
            imgs.append(image)
        except IOError:
            pass


repeated_pattern = find_ptrn(imgs)
size = sum(repeated_pattern)
canvas = Image.new('RGB', (size, size), 'white')

w, h = (255, 255)
x, y = (0, 0)

data = [['']]*len(repeated_pattern)
count = 0
trail = []

for i in imgs:
    W,H = i.size

    if count == 0:
        y = 0
    else:            
        y = data[count-1][1]

    if data[count][0]:
        x = data[count][0]
        if x == 255:
            tmp = 1

            while True:
                x = data[tmp][0]
                y = data[tmp-1][1]

                if W+x == 255:
                    canvas.paste(i, (x, y))
                    break
                else:                
                    tmp += 1
            continue

    canvas.paste(i, (x, y))
    data[count] = (W+x, H+y)

    if H+y == 255:
        count = 0
    else:
        count += 1

canvas.save('flag.png')
