import json
import signal
import subprocess
import socketserver
from hashlib import sha1
from random import randint
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
from ecdsa.ecdsa import curve_256, generator_256, Public_key, Private_key, Signature
import os


fnames = [b'subject_kolhen', b'subject_stommb', b'subject_danbeer']
nfnames = []


class ECDSA:
    def __init__(self):
        self.G = generator_256
        self.n = self.G.order()
        self.key = randint(1, self.n - 1)
        self.pubkey = Public_key(self.G, self.key * self.G)
        self.privkey = Private_key(self.pubkey, self.key)

    def sign(self, fname):
        h = sha1(fname).digest()
        nonce = randint(1, self.n - 1)
        sig = self.privkey.sign(bytes_to_long(h), nonce)
        return {"r": hex(sig.r)[2:], "s": hex(sig.s)[2:], "nonce": hex(nonce)[2:]}

    def verify(self, fname, r, s):
        h = bytes_to_long(sha1(fname).digest())
        r = int(r, 16)
        s = int(s, 16)
        sig = Signature(r, s)

        if self.pubkey.verifies(h, sig):
            return retrieve_file(fname)
        else:
            return 'Signature is not valid\n'


ecc = ECDSA()


def init_storage():
    i = 0
    for fname in fnames[:-1]:
        data = ecc.sign(fname)
        r, s = data['r'], data['s']
        nonce = data['nonce']
        nfname = fname.decode() + '_' + r + '_' + s + '_' + nonce[(14 + i):-14]
        nfnames.append(nfname)
        i += 2


def retrieve_file(fname):
    try:
        dt = open(fname, 'rb').read()
        return dt.hex()
    except:
        return 'The file does not exist!'


def challenge(req):
    req.sendall(b'This is a cloud storage service.\n' +
                b'You can list the files inside and also see their contents if your signatures are valid.\n')

    while True:
        req.sendall(b'\nOptions:\n1.List files\n2.Access a file\n')
        try:
            payload = json.loads(req.recv(4096))
            if payload['option'] == 'list':
                payload = json.dumps(
                    {'response': 'success', 'files': nfnames})
                req.sendall(payload.encode())
            elif payload['option'] == 'access':
                fname = payload['fname']
                r, s = payload['r'], payload['s']
                dt = ecc.verify(fname.encode(), r, s)
                if ('not exist' in dt) or ('not valid' in dt):
                    payload = json.dumps({'response': 'error', 'message': dt})
                else:
                    payload = json.dumps({'response': 'success', 'data': dt})
                req.sendall(payload.encode())
            else:
                payload = json.dumps(
                    {'response': 'error', 'message': 'Invalid option!'})
                req.sendall(payload.encode())
        except:
            payload = json.dumps(
                {'response': 'error', 'message': 'An error occured!'})
            req.sendall(payload.encode())


class incoming(socketserver.BaseRequestHandler):
    def handle(self):
        signal.alarm(30)
        req = self.request
        challenge(req)


class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


def main():
    init_storage()
    socketserver.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer(("0.0.0.0", 1337), incoming)
    server.serve_forever()


if __name__ == "__main__":
    main()
