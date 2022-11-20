from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

from netfilterqueue import NetfilterQueue
from base64 import b64encode, b64decode
from binascii import hexlify
from scapy.all import *
from config import *

import re
import os
import jwt
import json
import zlib
import struct
import random
import logging

logging.basicConfig(level=logging.DEBUG)

secret = None
sessions = {}

field = re.compile(r'PING(?P<payload>.*)(?P<token>.{4}TOKEN.*)', re.S)
sh_payload = re.compile(r'.{4}(?P<method>.{4})(?P<data>.*)(?P<crc>.{4})', re.S)
sh_token = re.compile(r'.{4}TOKEN(?P<data>.*)(?P<crc>.{4})', re.S)

def jsonify(**kwargs):
    return json.dumps(kwargs)

def pack(num):
    return struct.pack('!I', num)

def chsum(data):
    checksum = zlib.crc32(data) % (1<<32)
    return struct.pack('>I', checksum)

def randstr(seed, size=32):
    charset = 'abcdef0123456789'
    random.seed(seed)
    return str(bytearray(random.choice(charset) for _ in xrange(size)))

def encrypt(text, seed, session_id):
    key = randstr(seed + int(secret, 16) + int(session_id, 16)) 
    iv = os.urandom(16)
    aes = AES.new(key, AES.MODE_CBC, iv)

    text = pad(text, 16)
    data = aes.encrypt(text)

    return jsonify(iv=b64encode(iv), data=b64encode(data))

class EchoData(object):
    def __init__(self, type, data):
        self._data = zlib.compress(data)
        self._type = type

    def tobytes(self):
        return self.length + self.type + self.data + self.checksum

    @property
    def data(self):
        return self._data

    @property
    def type(self):
        return self._type 

    @property
    def length(self):
        return pack(len(self.data))

    @property
    def checksum(self):
        return chsum(self.data)


class Shell(object):
    def __init__(self, raw, seed):
        self._raw = raw
        self._seed = seed

        self._data = None
        self._token = None

    def run(self):
        col = field.search(self._raw)
        token = col.group('token')
        payload = col.group('payload')

        token = sh_token.search(token)
        token_data = token.group('data')
        token_crc = token.group('crc')

        payload = sh_payload.search(payload)
        payload_method = payload.group('method')
        payload_data = payload.group('data')
        payload_crc = payload.group('crc')

        assert (token_crc == chsum(token_data)), CRC_ERR
        assert (payload_crc == chsum(payload_data)), CRC_ERR

        token, data = map(
            lambda _ : json.loads(zlib.decompress(_)),
            (token_data, payload_data)
        )

        token = token.get('token')

        if payload_method == 'AUTH':
            self.auth(data, token)
        elif payload_method == 'SEND':
            self.send(data, token)

    def auth(self, data, token=None):
        global sessions, secret

        username = data['username']
        password = data['password']
        user = users.get(username)
        
        if user is None:
            raise Exception(INVALID_USER_ERR)
        if password != user.get('password'):
            raise Exception(INVALID_PASS_ERR)

        if not token:
            secret = randstr(random.getrandbits(8), size=5)
            session_id = randstr(random.getrandbits(8), size=32)
            sessions[session_id] = secret
        else:
            session_id = jwt.decode(token, secret).get('session_id')

        self.data = self.make_response_data('AUTH', LOGIN_SUCCESS, session_id)
        self.token = self.make_response_token('TOKEN', user, session_id, False)

    def send(self, data, token):
        global secret

        token_data = jwt.decode(token, secret)
        packet_data = b64decode(data.get('packet'))
        session_id = token_data.get('session_id')
        username = token_data.get('username')
        exhausted = token_data.get('exhausted')
        user = users.get(username)

        if session_id not in sessions:
            raise Exception(INVALID_SES_ERR)
        if exhausted:
            raise Exception(EXPIRED_SES_ERR)
        if not users.get(username)['is_admin']:
            raise Exception(INVALID_PRIV_ERR)

        response = sr1(IP(packet_data), timeout=1)
        if response:
            response = bytes(response)
        else:
            response = bytes('')
        
        secret = sessions[session_id]
        self.data = self.make_response_data('SEND', response, session_id)
        self.token = self.make_response_token('TOKEN', user, session_id, True)

    def make_response_data(self, method, content, session_id):
        encrypted_content = encrypt(
            str(content),
            self._seed,
            session_id
        )

        return EchoData(method, encrypted_content)

    def make_response_token(self, method, user, session_id, exhausted):
        token = jwt.encode({
            'session_id': session_id,
            'username': user.get('name'),
            'is_admin': user.get('is_admin'),
            'exhausted': exhausted
        }, secret)

        return EchoData(method, jsonify(token=token))
    
    @property
    def header(self):
        return 'PONG'

    @property
    def response(self):
        return self.header + self.data + self.token

    @property
    def data(self):
        return self._data.tobytes()

    @property
    def token(self):
        return self._token.tobytes()

    @data.setter
    def data(self, value):
        self._data = value

    @token.setter
    def token(self, value):
        self._token = value


def mod(pkt):
    time = int(pkt[IP].time)
    src = pkt[IP].src
    dst = pkt[IP].dst

    id = pkt[ICMP].id
    seq = pkt[ICMP].seq
    data = pkt[ICMP].load

    try:
        shell = Shell(data, int(time))
        shell.run()
        response = shell.response

    except Exception as e:
        stderr = EchoData('ERROR', str(e))
        response = stderr.tobytes()
        logging.error(str(e))

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