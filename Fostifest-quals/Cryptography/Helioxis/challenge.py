from hashlib import sha256
from random import randint
from Crypto.Util.number import *
from ecdsa.ecdsa import generator_brainpoolp256r1, Public_key, Private_key

G = generator_brainpoolp256r1
q = G.order()

FLAG = open('flag.txt', 'rb').read()


def genKeyPair():
    d = bytes_to_long(FLAG)
    assert d < q
    pubkey = Public_key(G, d * G)
    privkey = Private_key(pubkey, d)
    return pubkey, privkey


pubkey, privkey = genKeyPair()

for i in range(100):

    h = sha256(str(i).encode()).digest()
    k = randint(1, q - 1) >> 7
    signature = privkey.sign(bytes_to_long(h), k)
    verify = pubkey.verifies(bytes_to_long(h), signature)

    print(f"{i} = {(int(signature.r), int(signature.s), verify)}")
