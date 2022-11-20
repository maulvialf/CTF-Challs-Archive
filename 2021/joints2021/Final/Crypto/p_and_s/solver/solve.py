from pwn import *
from collections import Counter
from sys import stdout

len_flag = 46
target = 'localhost'
port = 5005

def encrypt(r,index):
    r.recvuntil('>>> ')       # menu utama
    r.sendline('2')                   # encrypt string sendiri
    r.recvuntil(' : ')        # Mau berapa kali ? : 
    r.sendline('5000')
    r.recvuntil(' : ')        # Masukan plaintext : 
    r.sendline('X'*len_flag)
    r.recvuntil(' : ')        # Ciphernya :

    cipher = r.recvuntil(']')[1:-1].decode().replace("'","").split(', ')

    charsAtIndex = [int(i[index].encode("latin-1").hex(),16) for i in map(lambda x: bytes.fromhex(x).decode("latin-1"),cipher)]
    charsAtIndex = Counter(charsAtIndex)
    
    newList = []                    # untuk menampung 10 most common beserta frekuensinya untuk perhitungan selanjutnya
    for i in charsAtIndex.most_common(10):
        for j in range(i[1]):
            newList.append(i[0])

    return newList

def encrypt_flag(r,index):
    r.recvuntil('>>> ')       # menu utama
    r.sendline('1')                   # encrypt flag
    r.recvuntil(' : ')        # Mau berapa kali ? : 
    r.sendline('5000')
    r.recvuntil(' : ')        # Ciphernya :

    cipher = r.recvuntil(']')[1:-1].decode().replace("'","").split(', ')

    charsAtIndex = [int(i[index].encode("latin-1").hex(),16) for i in map(lambda x: bytes.fromhex(x).decode("latin-1"),cipher)]
    charsAtIndex = Counter(charsAtIndex)
    
    newList = []                    # untuk menampung 10 most common beserta frekuensinya untuk perhitungan selanjutnya
    for i in charsAtIndex.most_common(10):
        for j in range(i[1]):
            newList.append(i[0])

    return newList

def main():
    flag = ""
    
    for i in range(len_flag):
        print(f"Char at {i}")
        r = remote(target,port)
        r.recvuntil('Secret : ')  # Masukan indeks untuk memasukan secret : 
        r.sendline(str(i))                   # index ke berapa yang mau diberi box istimewa

        tmp_list = []
        stdout.write("Searching Key")
        for j in range(10):             #setiap karakter diulang 10 kali 
            stdout.write('.')
            tmp_list += encrypt(r,i)
        
        tmp_list = Counter(tmp_list).most_common(1)[0][0]  # dapat cipher hasil xor 'X' dengan key
        key = ord('X')^tmp_list
        stdout.write("\n"+str(key))

        print("")

        tmp_list = []
        stdout.write("Searching Flag")
        for j in range(10):             #setiap karakter diulang 10 kali 
            stdout.write('.')
            tmp_list += encrypt_flag(r,i)
        tmp_list = Counter(tmp_list).most_common(1)[0][0]  # dapat most_common char ke i dari flag

        flag += chr(key^tmp_list)
        stdout.write("\n"+flag+'\n')
        r.close()

main()