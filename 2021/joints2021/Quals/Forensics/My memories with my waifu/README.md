# My memories with my waifu
Forensic:HARD
## Deskripsi
Bantulah menyelamatkan kenanganku bersama Isla
<br/>
--file integrity check--
<br/>
md5sum : f2f3b9fd4dfe0e45798b8bc99d0812ff
<br/>
crc32 : 1a6dba4e
## Hint (if needed)
1. waifumu 2D mz
2. RGBA(w:728)
*kalo kepepet banget ngga ada yang solve
## Note to panita
File soal: MEMORY.7z
<br/>
FLAG : JOINTS21{Pl4stiqu3_M3m0ry}

## How to solve
1. File extension .dmp (memdump) pakai volatility
2. untuk melihat memdump dari apa command : `vol.py -f MEMORY.dmp imageinfo`
3. untuk melihat proses yang jalan command : `vol.py -f MEMORY.dmp --profile=Win7SP1x86 pslist` \**param --profile dilihat dari image info*
4. ada mspaint.exe(PID:828)
5. Di-dump pake command: `vol.py -f MEMORY.dmp --profile=Win7SP1x86 memdump -p 828`
6. dari mspaint dump diubah jadiin .data(rawdata: memory sampah ngikut), trus pake gimp untuk buka. Dari sini nguli nyari parameter image yang pas.

<br/>
=-=Salah satu parameter GIMP yang paling enak dilihat:  =-=
<br/>
PID:`828` imageType: `RGBA`, offset:`6258760`, width: `728`, height: `406`
