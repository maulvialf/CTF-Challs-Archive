import os
import time
from aes import *


def encrypt(plaintext, key, n_rounds=10):

    assert len(plaintext) == 16
    plain_state = bytes2matrix(plaintext)

    key_matrices = expand_key(key, n_rounds)

    add_round_key(plain_state, key_matrices[0])
    sub_bytes(plain_state)

    for i in range(1, n_rounds):
        shift_rows(plain_state)
        mix_columns(plain_state)
        add_round_key(plain_state, key_matrices[i])

    sub_bytes(plain_state)
    shift_rows(plain_state)
    add_round_key(plain_state, key_matrices[-1])

    return matrix2bytes(plain_state)


if __name__ == '__main__':

    FLAG = open('flag.txt', 'r').read()

    banner = """
#################################################
#                                               #
#            Welcome to the Pantheon            #
#                                               #
#   Complete the challenge by send the correct  #
#                   master key                  #
#################################################
    """

    print(banner)
    print("Select your path:")
    print("[1] CELESTIAL")
    print("[2] DIVINE")
    print("[3] GODMASTER")
    print()
    path = input("> ")

    if path == '1':
        n_request = 20
        time_limit = 30
        realm = 'CELESTIAL'
    elif path == '2':
        n_request = 5
        time_limit = 600
        realm = 'DIVINE'
    elif path == '3':
        n_request = 5
        time_limit = 30
        realm = 'GODMASTER'
    else:
        print("There's no such path")
        exit()

    key = os.urandom(16)
    start = time.time()

    try:
        for n in range(n_request):
            message = bytes.fromhex(input("Msg to encrypt: "))
            encrypted = encrypt(message, key)
            print("> ", encrypted.hex())

        print("You have {} seconds to guess the key! Good luck!".format(time_limit))
        print()
        key_guess = bytes.fromhex(input("Guess the key: "))
        end = time.time()

        if end - start > time_limit:
            print("Too slow!!!")
            exit()

        if key == key_guess:
            print("-/\\- Congratulations! You have successfully ascended to the {} realm -/\\-".format(realm))
            print(FLAG)
        else:
            print("Mere human fail miserably...")
            exit()

    except Exception as e:
        print("No cheating >:(")
        exit()
