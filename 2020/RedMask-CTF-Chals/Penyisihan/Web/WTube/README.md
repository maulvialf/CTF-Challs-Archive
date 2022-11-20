## Judul Soal
WTube

## Deskripsi Soal
Mau nonton video dibayar dollar? ayo gabung ke WTube! <br>
Undang 15 orang untuk mendapatkan hadiah menarik.

## Hint Soal
- Nope

---

## Penjelasan Penyelesaian Soal

Sebenarnya tinggal invite 15 orang dengan email berbeda bakal dapet flag, tapi klo gitu gk soal ctf namanya wkwkwk.<br>
Poin yg ditekankan disini ialah vuln pendaftaran dengan email yang sama menggunakan email alias (+) <br>
Misalnya registrasi pake email `bambang+aaa@gmail.com` dan `bambang+bbb@gmail.com` <br>
Kedua email tersebut pada database sistem akan diidentifikasi sebagai email yang berbeda, sehingga valid saat registrasi. <br>
Akan tetapi, saat pesan konfirmasi dikirimkan, alamat email `bambang@gmail.com` akan mendapatkan dua pesan konfirmasi dari kedua email di atas yang menggunakan alias (+). <br>
Sehingga kita bisa mengeksploitasi sistem untuk mendaftar banyak akun hanya dengan bermodal satu alamat email.

<br>

## Solver

Ya tinggal otomasi aja pake python requests untuk registrasinya, nanti di emailnya tinggal klik link konfirmasinya satu per satu wkwkwk.