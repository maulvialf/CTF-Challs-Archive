## Judul Soal

Baby Remainder

## Deskripsi Soal

You know what to do with this baby, right?

## Hint Soal

- Problem utama dari challenge ini bukan pada bagian RSA
- Masih kehilangan beberapa bit plaintext? Kamu bisa menambahkan constraint dari informasi yang telah dimiliki

## Penjelasan Soal

Seperti pada judul, problem utama dari challenge ini adalah **Chinese Remainder Theorem** (CRT). Plaintext di-padding sehingga membuat plaintext terdiri dari kelipatan 16 bytes (pada kasus ini 64 bytes yang dapat diketahui dari bit-length modulus RSA). Namun padding pada kasus ini justru menimbulkan potensi _known-plaintext attack_ yang dapat membantu CRT menemukan nilai asli dari plaintext.
