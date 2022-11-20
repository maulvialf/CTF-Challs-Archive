## Judul Soal
memory

## Deskripsi Soal

> Poke the memories in the wasteland.<br><br>https://drive.google.com/drive/folders/1wtbSdq5UuY-WSBhGvoeXaL_ls6Di6jJB?usp=sharing<br><br>md5sum: e335b0ee6b0d57f68688b1674379aaa4
---

## Hint
- No Dupes Allowed
	(p.s.: Ada file berisi string yang sama berjumlah lebih dari 1, cukup 1 yang digunakan)
- https://www.youtube.com/watch?v=xond2K-7fjQ
	(p.s.: Judul: Sequence => Urutkan file yang didapatkan berdasar sequence)

---
## Proof of Concept

1. Cek profil
	vol.py -f memory.dmp imageinfo
2. Scan file
	vol.py -f memory.dmp --profile=Win7SP1x86_23418 filescan
3. Ada file notepad 'confide.txt' yang isinya link gdrive ke secret.zip
4. Scan Master File Table pake mftparser
	vol.py -f memory.dmp --profile=Win7SP1x86_23418 mftparser > mft-records
5. Dari teori deleted file di recycle bin, ada file $I (metadata) dan $R (actual data), extract files yang ada dari mft-records
	p.s: Ada metadata $I yang corrupt, ada $R yang duplikat. Cukup ambil file-file yang $I dan $R-nya tidak bermasalah
6. Ada 2 filename dari poin 5, RANDOM.txt dan SECRET.txt yang berjumlah banyak. Pisahkan terlebih dahulu ke RANDOM dan SECRET.
	p.s: cara cepat pakai `https://pypi.org/project/trashparse/`
7. File yang berasal dari SECRET.txt diurutkan berdasarkan deletion time (informasi deletion time didapat dari step 5 file $I), sehingga membentuk string 
	"KU4TINJDKJBWORDCGFWEYTKKN52GI3KIHFPEUJKRNBXWGOJGJQ4GGMRE"
8. Decode BASE32 string dari step 7 dan hasilnya dapat digunakan untuk unzip file secret.zip dari step 3

## Flag

JOINTS21{cr3at3_a_m3mdump_th3y_5a1d_it_w1ll_b3_fun_th3y_5a1d}

