from PIL import Image
import string
img = Image.open('./flag.txt.png')

background=[128,0,0]
w=img.load()
res=""
for p in range(img.size[0]):
	for q in range(img.size[1]):
		for i in range(3):
			res += bin(w[p,q][i])[-1]


def decompress(compressed):

    dict_size = 256
    dictionary = dict((chr(i), chr(i)) for i in range(dict_size))


    w = result = compressed.pop(0)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result += entry


        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result

e=[res[i:i+12] for i in range(0,len(res),12)]
p=[]
for i in e:
	t=int(i,2)
	if(t<=255):
		p.append(chr(t))
	else:
		p.append(t)

print(decompress(p))
