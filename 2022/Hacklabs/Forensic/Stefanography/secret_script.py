from Crypto.Util.number import *
from PIL import Image


flag = open('flag.txt','r').read()

imagi = Image.open('old_hekleb.png')
message = ''.join([bin((((bytes_to_long(x) & 0xff) << 8) | (bytes_to_long(x) >> 8)))[2:].zfill(16) for x in [flag[i:i+2].encode() for i in range(0,len(flag),2)]])

c = 0
try:
	w, h = imagi.size
	for x in range(0, w):
		for y in range(0, h):
			pixel = list(imagi.getpixel((x,y)))
			for channel in range(0,3):
				if (c < len(message)):
					pixel[channel] = pixel[channel] & 0 |  int(message[c])
					c += 1
			imagi.putpixel((x,y), tuple(pixel))
	imagi.save("hekleb.png", "PNG")
except Exception as e:
	print(e)