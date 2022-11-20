# Where is the file
Forensic : MED-Easy
## Deskripsi
Polisi menangkap pengedar ℌệ𝔫𝔱ằ𝔦. Saat ingin mengambil bukti berupa harddisk milik pelaku, pelaku sempat memberontak dan menyentuh komputernya selama beberapa detik. Bantulah pak polisi agar dapat ~~menonton ℌệ𝔫𝔱ằ𝔦~~ menunjukkan barang bukti. 

## Note to panita
File soal: disk.zip
<br/>
FLAG : JOINTS21{H3al_th3_D3geN3r4te_DI5K}

## How to solve
1. ada 4 file dump disk
2. ternyata raid 5
3. disk3 broken
4. mount disk1,2,4 ke dev/loop
5. force assemble disk yang tadi di mount

