# Desc

TryCallMe

# Note untuk panitia

- Versi OS adalah Ubuntu 20.04
- Peserta diberikan binary yang sudah dicompile (TryCallMe) di folder attachment

# Flow singkat solver

Terdapat fungsi TryCallMe yang menerima 10 argumen yang akan memberikan flag jika argumen yang diberikan sesuai dengan yang diminta. Selain itu terdapat buffer overflow di fungsi main. Karena pada program 64bit argumen fungsi disimpan di register dan di fungsi TryCallMe register tersebut akan disimpan pada stack, maka kita dapat mengisi stack dengan nilai argumen dan melakukan jump ke tengah-tengah fungsi TryCallMe setelah semua argumen disimpan di stack. Kita dapat menggunakan ret2csu untuk memanggil fungsi write untuk membuat stack palsu di segment .bss dan melakukan pivoting stack ke segment tersebut. Terakhir, kita lakukan return ke tengah-tengah fungsi TryCallMe.

# Flag

JOINTS21{C0n6RaT5_y0u_c4n_CaLl_M3}