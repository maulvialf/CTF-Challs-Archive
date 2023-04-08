#!/usr/bin/python3
from Crypto.Util.number import *
import random
from math import gcd
from redacted import flag
base = 64

def enc1():
    pl = random.getrandbits(base)
    p,q = getPrime(base), getPrime(base)
    e = 0x10001
    assert gcd(e, p*q)==1
    return [pow(pl,e,p*q), p*q]

def enc2():
    pl = random.getrandbits(base)   
    p = getPrime(base*16)
    q = p+2
    while(isPrime(q)==0):
        q+=((base//32)^0x1-1)
    e = 0x10001
    assert gcd(e, p*q)==1
    return [pow(pl,e,p*q), p*q]

def enc3():
    pl = random.getrandbits(base)   
    p = getPrime(base*16)
    q = getPrime(base*16)
    e = 0x10001
    assert gcd(e, p*q)==1
    return [pow(pl,e^0x1000e,p*q), p*q]

def enc4():
    pl = random.getrandbits(base)  
    p = getPrime(base*16)
    q = getPrime(base//16)
    e = 0x10001
    assert gcd(e, p*q)==1
    return [pow(pl,e,p*q), p*q]

def mainMap():
    inc = 0
    funfdata = [enc1, enc2, enc3, enc4]
    while True:
        inc+=1
        if(inc==312):
            print("YOUUU TRY TOOO MUCH!!!! WANNA BREAK MY COMPUTER??")
            break
        print("[1] trying\n[2] what is flag?\n[3] exit")
        data = input("YOU WANT what MENUS? :")
        if(data=='3'): break
        elif(data=='2'):
            p = random.getrandbits(512)
            q = random.getrandbits(512)
            if(p%2==0): p+=1
            if(q%2==0): q+=1
            while(isPrime(q)==0):
                q+=((base//32)^0x1-1)
            while(isPrime(p)==0):
                p+=((base//32)^0x1-1)
            e = 0x10001
            assert gcd(e, p*q)==1
            print([pow(bytes_to_long(flag),e,p*q), p*q])
        else:
            rand = random.getrandbits(32)
            print(funfdata[rand%4]())
            print(f'encryption id #{rand//4+inc}')

mainMap()