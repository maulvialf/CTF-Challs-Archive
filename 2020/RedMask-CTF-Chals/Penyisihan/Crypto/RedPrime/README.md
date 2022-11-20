## Judul Soal

Red Primes

## Deskripsi Soal

Kalo ada cara ribet kenapa harus gampang?

## Hint Soal

- The fractions is less than one.

## Penjelasan Soal

Inspired by ASIS CTF Finals 2019 - Serifin

_Sum of an infinite geometric series_ dimana `Fraction(11, 17)` dan `Fraction(13, 19)` jelas lebih kecil dari 1. Gunakan rumus `a/(r-1)` untuk mencari persamaan, dengan begitu kita bisa dapatkan kembali nilai x dari n. Gunakan `genPrime(x)` untuk mendapatkan p dan q. Sebenernya nilai x yang didapat gak begitu akurat, tapi salah satu prime q masih bisa didapat dari nilai x tersebut. Balikin p tinggal `n/q`, sisanya dekrip RSA biasa.
