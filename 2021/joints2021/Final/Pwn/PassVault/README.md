# Desc

Some "password manager" program.

# Note untuk panitia

- Versi OS adalah Ubuntu 20.04
- Peserta diberikan binary yang sudah dicompile (PassVault) dan file libc (libc.so) di folder attachment.

# Flow singkat solver

Terdapat vuln oob dimana tidak ada pengecekan index negatif dan fungsi sigill_handler yang akan memberikan nilai RIP saat terjadi SIGILL. Kita dapat mengoverwrite GOT exit dengan address main (dengan brute force 1 nibble) untuk kembali ke fungsi main saat sigill_handler dipanggil. Untuk melakukan leak address libc, address memset di GOT dapat diubah sedemikian rupa sehingga instruksi yang akan dikalankan tidak valid dan menyebabkan SIGILL. Setelah mendapatkan address libc, kita dapat mengoverwrite GOT memset dengan address system dan menghapus entry yang memiliki string "/bin/sh".

# Flag

JOINTS21{Ch3cK_F0r_n36At1V3_Valu3}