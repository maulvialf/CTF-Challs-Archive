from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

from binascii import unhexlify
from subprocess import PIPE, Popen
from scapy.all import *

import re
import os
import zlib
import struct
import random

timestamp = None
command = None
results = {}

def get_key(seed, size=32):
    random.seed(seed)
    return bytearray(random.getrandbits(8) for _ in xrange(size))

def decrypt(ciphertext, seed):
    iv = ciphertext[:16]
    text = ciphertext[16:]

    key = get_key(seed)
    aes = AES.new(key, AES.MODE_CBC, iv)
    
    return unpad(aes.decrypt(text), 16)

def icmp_exfil(packet):
    global command
    global timestamp
    global results

    icmp_data = packet[ICMP].load
    matches = data_exfil.findall(icmp_data)[0]

    prefix, data  = matches
    decoded_data = zlib.decompress(data)

    if prefix == 'PING':
        command = decoded_data
        timestamp = int(packet[IP].time)
    
    elif prefix == 'PONG':
        while True:
            try:
                plaintext = decrypt(decoded_data, timestamp)
                if not re.match(r'^[a-f0-9]+$', plaintext):
                    raise Exception
            except:
                timestamp -= 1
            else:
                results[command] = unhexlify(plaintext)
                break  

data_exfil = re.compile(r'.{4}(PING|PONG)(.*).{4}', re.S)
dd_exfil = re.compile(r'dd if=(.+) bs=(\d+) skip=(\d+) count=(\d+)')
packets = rdpcap('shell.pcap')

for packet in packets:
    if data_exfil.match(packet[ICMP].load):
        icmp_exfil(packet)

content_files = {}
for key, val in results.items():
    if dd_exfil.match(key):
        matches = dd_exfil.findall(key)[0]
        filename, bs, skip, count = matches

        content = content_files.get(filename, [''] * 9999)
        if not content[0]:
            content_files[filename] = content

        bs, skip, count = map(int, (bs, skip, count))
        index = bs * skip

        content[index] = val

for name, content in content_files.items():
    with open(os.path.basename(name), 'wb') as f:
        f.write(''.join(content))