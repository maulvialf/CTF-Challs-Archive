# IDE
Tujuannya chall ini adalah melakukan RCE dengan memanfaatkan isi file kemudian menjalankan command sh pada file tersebut. Manfaatkan param echo untuk menginputkan tiap byte/char payload. Manfaatkan param echo1 untuk menyimpan byte/char tersebut kedalam sebuah file. Manfaatkan fungsi sh untuk menjalankan RCE.Perhatikan juga limit char yang bisa diinputkan.

1. List directory
Manfaatkan fungsi ls untuk mencari directory flag
2. Sendpayload
Hasil dari listing directory disimpan pada file tertentu kemudian bisa memanfaatkan curl untuk mengrim request via requestbin atau semisal.
