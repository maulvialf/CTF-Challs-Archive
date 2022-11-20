from PIL import ImageDraw
from PIL import Image
import random
def llhohlo(llIllllIl):
    lul=256
    bruh = dict((chr(i), chr(i)) for i in range(lul))
    brah = ""
    yes = []
    for yooyo in llIllllIl: 
        moo = brah + yooyo
        if moo not in bruh:
            yes.append(bruh[brah])
            
            bruh[moo] = lul
            lul += 1
            brah = yooyo
        else:
            brah = moo

    if brah:
        yes.append(bruh[brah])
    return yes


W,H=(256,256)
new = Image.new("RGB", (W,H),(128,0,0))
d=ImageDraw.Draw(new)
flag="flag.txt"
w,h=d.textsize(flag)
d.text(((W-w)/2,(H-h)/2),flag,fill="black")
y=new.load()



x=open(flag).read()

tes =llhohlo(x)

b_message=''.join([format(ord(i) if type(i)==str else i, "012b") for i in tes])




index=0
for p in range(new.size[0]):
	for q in range(new.size[1]):
		val=[]
		for i in range(3):
			if(index>=len(b_message)):
				val.append(y[p,q][i])
			else:
				val.append(y[p,q][i]|int(b_message[index]))
				index+=1


		y[p,q]=tuple(val)

new.save(flag+'.png',"PNG")

