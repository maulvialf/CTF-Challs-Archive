# Inui Toko [1000 pts]

**Category:** Pwn
**Solves:** 0

## Description
>gatau masukin apa kesini\r\n\r\ngood luck aja deh\r\n\r\nchallenge di build pake ubuntu 22.04 latest, jadi kalo ada salah offset dsb silakan build di local\r\n\r\nAuthor: Zafirr

**Hint**
* randomizernya: https://www.geeksforgeeks.org/stdmt19937-class-in-cpp/\n\nchecksum disimpan di loker tapi ada off by one keknya\n\npartial relro + no pie, you know what to do :eyes:\n* overwrite got nya gak sekali, tapi 2 kali!!!!! :scream: :scream: :scream:\n* change delete to call the plt of another function. \nchange that other function to system\ncall delete\nprofit

## Solution

### Flag

