## Judul Soal

Drakjoge

## Deskripsi Soal

Kamu adalah seorang komedian yang ingin mendaftar ke salah satu komunitas komedi yang cukup terkenal, yaitu Indonesian Drakjoge. Namun pada saat mendaftar, kamu dihadapkan dengan seorang Bang Haxor, salah satu sesepuh di komunitas Indonesian Drakjoge. Bang Haxor tidak bisa menerima kamu ke komunitas jika kamu tidak mengerti apa yang ia katakan. Ayo buktikan kalau kamu layak berada di komunitas Indonesian Drakjoge!

nc HOST PORT

## Hint Soal

- Cyclic.calc adalah CRC32

## Penjelasan Soal

Seperti MODE ECB pada umumnya, byte flag bisa direcover secara satu per satu dengan memanfaatkan per potongan block. Byte flag bisa direcover baik dari depan maupun dari belakang. Namun pada kasus ini, 4 byte yang dihasilkan oleh CRC tidak bisa kita tebak sehingga byte flag hanya bisa direcover dari belakang, dengan catatan harus mengetahui panjang flag terlebih dahulu. Panjang flag bisa diketahui dengan memanfaatkan banyaknya byte input yang kita masukkan, lalu bandingkan berapa banyak block yang dihasilkan oleh Bang Haxor.
