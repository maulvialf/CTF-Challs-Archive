# Paket.... ashiap
Forensic : HARD
## Deskripsi
Server mihoho kebobolan, cari tau apa yang dicuri
<br/>
--file integrity check--
<br/>
md5sum : 619bd9a9b3b51d9ad43e132753d5980a

## Hint
1. Pintu belakang
2. AES 128
*kalo kepepet banget ngga ada yang solve
## Note to panita
File soal: packet.pcapng
<br/>
FLAG : JOINTS21{WHY_using_BlueTooth}

## How to solve
1. Liat http post data yang menuju /b3kd0r
2. Decode post data yang ada. format: `AES128 <key>.<encoded>`
3. keliatan command command ke backdoor
4. dump data bluetooth(ada 3x transmisi) -> hapus header -> gabungin jadi 3 file (ini agak susah)
5. rename sesuai commands yang didapetin tadi
6. buka zip pake password dari no 3


