#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import json, signal, sys

class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

FLAG = open('flag.txt', 'rb').read()

BUBUR = {
    "diaduk": "semua rasa tercampur dengan sempurna",
    "tidak diaduk": "terlihat dan terjaga tetap estetik",
    "diblender": FLAG.decode()
}

key = AES.get_random_bytes(AES.block_size)

def user_input(s):
    inp = input(s).strip()
    assert len(inp) < 1024
    return inp

def tulis():
    try:
        nama = user_input('Nama: ')
        sekte = user_input('Sekte (diaduk/tidak diaduk): ')
        assert sekte in ['diaduk', 'tidak diaduk']
        alasan = BUBUR[sekte]
        rating = int(user_input('Rating (1-5): '))
        assert rating in [1, 2, 3, 4, 5]
    except:
        print('Review kamu aneh, silakan coba lagi')
        return

    form = json.dumps({
        "nama": nama,
        "sekte": sekte,
        "alasan": alasan,
        "rating": rating
    }).encode()

    enc = AES.new(key, AES.MODE_ECB).encrypt(pad(form, 16))
    kupon = enc.hex()
    print('Kamu bisa gunakan kupon di bawah ini untuk mendapatkan bubur gratis!')
    print('Kupon: ' + kupon)

def redeem(kupon):
    try:
        dec = AES.new(key, AES.MODE_ECB).decrypt(bytes.fromhex(kupon))
        form = json.loads(unpad(dec, 16))
        assert "sekte" in form.keys() and "alasan" in form.keys() and "rating" in form.keys()

        form["alasan"] = BUBUR[form["sekte"]]

        if form["sekte"] == "diblender" and form["rating"] == 5:
            print(f'Mencengangkan! Kamu suka makan bubur {form["sekte"]} karena {form["alasan"]}?')
        else:
            print(f'Kupon berhasil digunakan! Bubur gratis untuk kamu: {chr(0x1f372)}')
    except:
        print('Kupon yang kamu miliki tidak berasal dari Warung Bubur MDT')
        return

def banner():
    print('-' * 60)
    print('Selamat datang di Warung Bubur MDT')
    print('Warung Bubur MDT sedang mengadakan event tulis review bubur')
    print('Setiap review yang kamu tulis dapat ditukarkan dengan 1 porsi bubur gratis')
    print('Review terbaik akan mendapatkan hadiah spesial dari Warung Bubur MDT')
    print('-' * 60)
    print('Kamu bisa:')
    print('1. Tulis review')
    print('2. Redeem kupon')

def main():
    banner()
    ink = 100
    used = []
    while True:
        print('-' * 60)
        opt = user_input('> ')
        if opt == '1':
            if ink >= 30:
                tulis()
                ink -= 30
            else:
                print('Tinta pulpenmu tidak cukup untuk menulis review lagi')
        elif opt == '2':
            coupon = user_input('Kupon: ')
            if coupon in used:
                print('Kupon telah digunakan')
            else:
                redeem(coupon)
                used.append(coupon)
        else:
            break

if __name__ == '__main__':
    signal.alarm(60)
    main()
