Description:
Return Oriented Programming (ROP) adalah salah satu trik yang biasa digunakan untuk mengeksekusi kode ketika instruction pointer sudah dapat dikontrol namun memasukkan/mengeksekusi shellcode tidak memungkinkan. Ide dasar ROP adalah menggunakan potongan-potongan instruksi mesin pada binary ataupun library yang mengandung ret (return) atau call (termasuk syscall) yang biasa disebut dengan ROP gadgets. Gadgets tersebut disusun sedemikian rupa sehingga instruksi bisa lompat-lompat dan pada akhirnya mengeksekusi perintah yang kita inginkan.

Berikut adalah layanan yang memilik celah buffer overflow tanpa proteksi canary (stack protector) sehingga Anda dapat meng-overwrite instruction pointer mulai dari bytes ke-17 input. Binary ini di-compile secara statically-linked, tetapi Anda tidak punya akses ke binary-nya. Yang Anda dapatkan hanya informasi mengenai binary ELF tersebut dan juga kumpulan alamat gadgets yang bisa Anda gunakan.

`nc pwn.cyber.jawara.systems 13372`

Hint:
