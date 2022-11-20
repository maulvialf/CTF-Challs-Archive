import sys
import base64
import struct
import binascii


def KSA(key):
    keylength = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # swap
    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(s, key):
    S = KSA(key)
    X = PRGA(S)
    return bytes([x ^ next(X) for x in s])


if __name__ == '__main__':

    key = b"REDACTED"
    flag = b"REDACTED"
    crc = struct.pack("I", binascii.crc32(flag))

    m = flag + crc
    m_enc = RC4(m, key)

    print()
    print("Dekripsikan cipher text berikut: {}".format(base64.b64encode(m_enc).decode()))
    print()
    print("Masukkan base64(RC4(p + checksum(p), unknown_key))")
    while True:
        try:
            a = input(">> ")
            a = base64.b64decode(a)

            m_dec = RC4(a, key)
            m_dec_p   = m_dec[:-4]
            m_dec_crc = m_dec[-4:]

            if struct.pack("I", binascii.crc32(m_dec_p)) == m_dec_crc:
                print("Valid")
            else:
                raise Exception()
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            print("Tidak valid")
    print()

