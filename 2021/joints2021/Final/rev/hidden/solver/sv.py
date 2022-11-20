from pwn import *
context.terminal="tmux splitw -h".split()

r=process('./finished',aslr=False)
gdb.attach(r,"""awatch *0x407080
	set logging file gdb.txt
	c
	fin
	set logging on
	p/s (unsigned char[100]) *0x407080
	set logging off
	ni
	ni
	ni
	ni
	ni
	ni
	set $rax=1
	"""*63+"""c
	quit
	""")
r.sendline('a'*63)
r.interactive()
x=open('./gdb.txt').readlines()
y=open('./res.txt','w+')
for i in x:
	print(i[i.index("\"")+1:i.index(", '\\000'")-1].decode("string-escape").encode("hex"))
	y.write(i[i.index("\"")+1:i.index(", '\\000'")-1].decode("string-escape").encode("hex")+'\n')


