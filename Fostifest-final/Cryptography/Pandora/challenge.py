import os
from aes import *

FLAG = open('flag.txt', 'rb').read()


def encrypt_block(plaintext, key, n_rounds=4):

    assert len(plaintext) == 16
    plain_state = bytes2matrix(plaintext)

    key_matrices = expand_key(key, n_rounds)

    add_round_key(plain_state, key_matrices[0])

    for i in range(1, n_rounds + 1):
        sub_bytes(plain_state)
        shift_rows(plain_state)
        mix_columns(plain_state)
        add_round_key(plain_state, key_matrices[i])

    return matrix2bytes(plain_state)


def encrypt_ecb(plaintext, key):
    plaintext = pad(plaintext)

    blocks = []
    for plaintext_block in split_blocks(plaintext):
        block = encrypt_block(plaintext_block, key)
        blocks.append(block)

    return b''.join(blocks)


if __name__ == '__main__':

    key = os.urandom(16)

    msg = bytes.fromhex(input('Your msg >> '))

    assert len(msg) <= 4080, "Your msg too long"

    print('Encrypted msg :', encrypt_ecb(msg, key).hex())

    key_guess = bytes.fromhex(input('Guess key >> '))

    if key == key_guess:
        print(FLAG)
