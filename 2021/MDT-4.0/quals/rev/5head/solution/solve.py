from PIL import Image, ImageDraw

def encode(data):
    cnt = 1
    out = []
    cur = data[0]
    for i in data[1:]:
        if cur == i:
            cnt += 1
        else:
            out.append((cnt << 8) + cur)
            cur = i
            cnt = 1
    out.append((cnt << 8) + cur)
    return out

def decode(data):
    out = []
    for i in data:
        out += [(i & 0xff)] * (i >> 8)
        
    return out


data = eval(open("array").read())
arr = decode(data)
rgba = [tuple(arr[i:i+4]) for i in range(0,len(arr),4)]

img = Image.new('RGBA', (480, 640))
cnt = 0

for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):
        b, g, r, a = rgba[cnt]
        img.putpixel((i, j), (r,g,b,a))
        cnt += 1
        
img = img.transpose(Image.ROTATE_270)
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img.show()

