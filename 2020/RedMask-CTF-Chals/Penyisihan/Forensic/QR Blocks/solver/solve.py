from pyzbar.pyzbar import decode
from textwrap import wrap
from PIL import Image
from zlib import crc32

import struct

class Chunk:
    def __init__(self, data, pos):
        self.size = self.get_size(data)
        self.type = self.get_type(data)
        self.data = self.get_data(data)
        self.crc  = self.get_crc(data)

    def get_size(self, data):
        return data[:4]

    def get_type(self, data):
        return data[4:8]

    def get_data(self, data):
        return data[8:-4]

    def get_crc(self, data):
        return data[-4:]

    @property
    def chunks(self):
        return [self.size, self.type, self.data + self.crc]

    @property
    def raw(self):
        return ''.join(self.chunks)

def calc_crc32(data):
    checksum = crc32(data) % (1<<32)
    return struct.pack('>I', checksum)

def parse_chunk(pos, length, content):
    begin, end = (pos, pos+length)
    content = content[begin: end]
    pos = len(content)

    return Chunk(content, pos), pos

def bytes_to_long(data):
    return struct.unpack('!I', data)[0]

def calcSize(size, offset):
    sizes = []
    for x,y in zip(size, offset):
        sizes.append((x[0]+y[0],x[1]+y[1]))
    return max(sizes)

def iterate_chunk(content):
    chunks = []
    pos = 8

    while pos < len(content):
        try:
            begin, end = (pos, pos+4)
            length = struct.unpack('!I', content[begin: end])[0]
            res = parse_chunk(pos, length + 12, content)

            chunks.append(res[0])
            pos += res[1]
        except struct.error:
            break

    return chunks

with open('qr.png') as img:
    image = img.read()

chunks = iterate_chunk(image)
head = image[:8]
ihdr = chunks[0].raw
iend = chunks[-1].raw

offs = [i for i in chunks[1::2] if i.type == 'oFFs']
idat = [i for i in chunks[2::2] if i.type == 'IDAT']
size = [(50,50)] * len(idat)

for enum, block in enumerate(zip(offs, idat)):
    offset = block[0].data[:-1]
    crc = map(lambda x: calc_crc32(x.raw[4:-4]), block)
    x,y = map(lambda x : bytes_to_long(x), wrap(offset, 4))

    idat[enum] = map(lambda  x,y: x.raw[:-4] + y , block, crc)
    offs[enum] = (x,y)

dimension = calcSize(size, offs)
image = Image.new('RGB',dimension)

for offset, data in zip(offs, idat):
    with open('tmp.png','wb') as file:
        file.write(head + ihdr + ''.join(data) + iend)

    img = Image.open('tmp.png')
    image.paste(img, offset)

image.save('flag.png')
print decode(image)[0].data 
