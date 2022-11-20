from multiprocessing import Pool
from pwn import *

def login(username):
    r = remote('0.0.0.0', '22222', level='error')
    r.sendlineafter('username:', username)
    r.sendlineafter('password:','12345')
    
    try:
        r.sendlineafter('$', 'whoami', timeout=3)
        print(f'Sending command on {username} -> Work')
    except:
        print(f'Sending command on {username} -> Error')

uname = [f'test_soal{i}' for i in range(1,16)]

with Pool(15) as p:
    p.map(login, uname)
