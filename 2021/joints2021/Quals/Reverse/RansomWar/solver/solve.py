from pwn import xor
import math
import pyperclip


def decryptMessage(cipher,key): 
    msg = "" 
  
    k_indx = 0
  
    msg_indx = 0
    msg_len = len(cipher)
    msg_lst = list(cipher) 
  
    col = len(key) 
      
    row = int(math.ceil(msg_len / col)) 
  
    key_lst = sorted(list(key)) 
  
    dec_cipher = [] 
    for _ in range(row): 
        dec_cipher += [[None] * col] 
  
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
  
        for j in range(row): 
            dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
            msg_indx += 1
        k_indx += 1
  
    try: 
        msg = ''.join(sum(dec_cipher, [])) 
    except TypeError: 
        raise TypeError("This program cannot", 
                        "handle repeating words.") 
  
    null_count = msg.count('_') 
  
    if null_count > 0: 
        return msg[: -null_count] 
  
    return msg 

for i in range(100):
    key = open('../chall/key/key{0}'.format(i), 'rb').read()
    cipher = "30435993e440b462fc33493bef977c0afa93db54".decode('hex')
    cipher = xor(cipher, key)
    cipher = cipher[::-1]
    plain = decryptMessage(cipher,'32145')
    if 'JOINTS21' in plain:
        print(plain)
        break