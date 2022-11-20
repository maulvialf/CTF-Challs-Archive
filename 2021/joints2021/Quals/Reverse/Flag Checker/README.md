# Desc

I created a ~~password~~ flag checker program. Try to understand it's implementation to get my ~~password~~ flag.

# Note untuk panitia

- isi folder `attachement` diberikank kepada peserta

# Flow singkat solver

Charset yang digunakan hanya `qwertyuiopasdfghjklzxcvbnm0123456789_`. Secara sederhana, program membagi flag menjadi beberapa bagian, lalu melakukan semacam algoritma `hashing` untuk tiap bagian nya. Setelah itu diconcat (dijamin hasil hash memiliki panjang 3 byte).

Intended solution adalah dengan bruteforce karena charset yang digunakan cukup kecil dan input yang dipakai untuk tiap blok nya juga kecil.

# Flag

JOINTS21{just_an0ther_stup1d_c0d3}
