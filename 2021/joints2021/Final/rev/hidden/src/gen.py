import random
import os
import re
import string
from pwn import *
# from z3 import *
flag="ResidentSleeper_EZ_Clap_TriHard_HACKERMANS_NotLikeThis_BabyRage"
cp_flag=list(flag)
x=list(map(ord,cp_flag))
compile_cmd="gcc -fno-pie -no-pie -fpic  -Wno-implicit-function-declaration ./build/hmm.c -o ./build/hmm"
compile_finish="gcc -fno-pie -no-pie -fpic -Wno-implicit-function-declaration ./build/finished.c -o ./build/finished"

main="""void main(){{
	printf("%d",R("{}"));
}}
""".format(flag)

head="""#include<stdio.h>
"""

template="""
int {}(char x[]){{
	if((long)({}) != {}){{
		return 0;
	}}
	return 1 ;
}}
"""

pp=""
operations={1:["{} + {}","{} ^ {}","{} * {}"],
2:["{} + {}","{} * {}","{} - {}","{} ^ {}","{} & {}"]}
# 3:["{}*{} ^ {}","({} ^ {}) * {}", "({} + {}) | {}"],
# 4:["{} * {} + {}^{}"]}
leng=len(flag)
for i in range(leng):
	numb = 1
	op_choice = random.choice(operations[numb])
	nums=["x[{}]".format(i%len(flag))]
	if(numb==2):
		nums.append("x[{}]".format(random.randint(0,len(flag)-1)))
		res=op_choice.format(nums[0],nums[1])
	elif(numb==3):
		nums.append("{}".format(random.randint(1,5)))
		nums.append("x[{}]".format(random.randint(0,len(flag)-1)))
		res=op_choice.format(nums[0],nums[1],nums[2])
	elif(numb==4):
		nums.append("x[{}]".format(random.randint(0,len(flag)-1)))
		nums.append("x[{}]".format(random.randint(0,len(flag)-1)))
		nums.append("{}".format(random.randint(1,5)))
		res=op_choice.format(nums[0],nums[1],nums[2],nums[3])
	elif(numb==1):
		nums.append("{}".format(random.randint(1,200)))
		res=op_choice.format(nums[0],nums[1])
	name = flag[:i+1]
	# if(i==len(flag)-1):
	# 	retur="1"
	# else:
	# 	retur=flag[:i+2]+'(x)'
	pp += template.format(name,res,eval(res))

	


sc = head + pp+main

x=open('./build/hmm.c','w+')
x.write(sc)
x.close()

os.system(compile_cmd)

yes = os.popen('objdump -D -M intel ./build/hmm').read().split('0000000000')[20:20+len(flag)]
regex=":\t(.+)?\t"

head2="""#include<stdio.h>
#include<string.h>
unsigned char code[]="{}";
"""
template2="""int {}(unsigned char x[]){{
	unsigned char p[]="{}";
	for(int i=0;i<={};i+=1){{
		p[i]^='\\x{}';
	}}
	memcpy(code,p,{});
	int (*www)(char po[]) = (int(*)(char po[]))code;
	if(www(x)){{
		return {};
	}}
	return 0;
}}
"""
names=[''.join(random.sample(string.letters,16)) for i in range(len(flag))]
# print(len(names))
main2="""void main(){{
	mprotect(0x407000,0x1000,0x7);
	char inp[{}];
	char flag[{}];
	fgets(inp,sizeof(inp),stdin);
	sscanf(inp,"JOINTS21{{%s}}",flag);
	if({}(flag)){{
		printf("Nice! JOINTS21{{%s}}\\r\\n",flag);
	}}else{{
		printf("Too bad\\r\\n");
	}}
}}
""".format(len(flag)+len("JOINTS21{}"),len(flag)+len("JOINTS21{}"),names[0])

pp=""
maks=0

for i in range(len(yes)):
	num=random.randint(0,255)
	opcodes = re.findall(regex,yes[i])
	# name = flag[:i+1]
	name=names[i]
	if(i==len(yes)-1):
		retur="1"
	else:
		retur=names[i+1]+'(x)'
	parsed=""
	for k in opcodes:
		parsed+=k.replace(" ","")
	if(i==0):
		print( yes[i])
		print (parsed)
	parsed=xor(parsed.decode("hex"),num).encode("hex")
	length=len(parsed)//2
	maks=max(maks,length)
	parsed=''.join(["\\x"+parsed[w:w+2] for w in range(0,len(parsed),2)])
	pp+=template2.format(name,parsed,length,hex(num)[2:],length,retur)
	if(i==0):
		print (pp)
t='00'*maks	
t=''.join(["\\x"+t[w:w+2] for w in range(0,len(t),2)])
sc = head2.format(t)+pp+main2
x=open('./build/finished.c','w+')
x.write(sc)
x.close()

os.system(compile_finish)
