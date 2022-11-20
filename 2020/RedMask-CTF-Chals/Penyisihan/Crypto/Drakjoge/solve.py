from deom import *
import string

# p = process('./server.py')
p = remote('localhost', 30001)

def kirim(x):
  p.sendlineafter('Kamu: ', s2b(x))
  p.recvuntil('Bang Haxor: ')
  res = p.recvline().strip()
  return b2s(res).encode('hex')

def panjang_flag():
  for i in range(1, 16+1):
    res = kirim('z' * i)
    print i, len(res)

def potong(x):
  res = []
  for i in range(0, len(x), 32):
    res.append(x[i:i + 32])
  return res

panjang_flag()
LEN_FLAG = 128 / 2 - 13 - 4
JUNK = -(LEN_FLAG + 4) % 16
flag = ''
ctr = 0

while True:
  for i in range(16):
    payload = 'z'*(JUNK + i + 1)
    correct_block = kirim(payload)
    correct_block = potong(correct_block)[-ctr-1]
    for c in string.printable:
      payload = c + flag + chr(16 - i - 1) * (16 - i - 1)
      test_block = kirim(payload)
      test_block = potong(test_block)[0]
      if test_block == correct_block:
        flag = c + flag
        print flag
        if flag.startswith('redmask{'):
          p.close()
          exit()
        if len(flag) % 16 == 0:
          ctr = 0
        break
  ctr += 1
