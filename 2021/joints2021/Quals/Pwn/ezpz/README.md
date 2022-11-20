# Desc

A simple program to get you started

# Note untuk panitia

- isi folder `attachement` diberikank kepada peserta
- port chal: `22221`
- buat run, masuk ke folder source, terus `docker-compose up -d`

# Flow singkat solver

Recon:

- PIE non aktif
- Diberikan address stack
- Ada vuln off by one
- Terdapat fungsi win (`0x4011f6`) yang melakukan cat flag
- Fungsi selain fungsi `win` semuanya berada pada address `0x4012XX`

Karena address fungsi `win` memiliki sedikit di atas address fungsi lain, dan kita hanya memiliki one byte overflow, kita tidak dapat langsung return ke fungsi `win`. Intended solution di sini adalah dengan mengkalkulasi nilai `rbp` fungsi `vuln` dari address stack yang diberikan di awal. Kemudian lakukan one byte overflow pada return address serta ubah nilai `rbp` ke `rbp+0x38` (sehingga kita dapat return ke address yang berawalan `0x4011` -> didapat dari debugging). Setelah itu tinggal lakukan buffer overflow lagi (overwrite 1 byte return address menjadi `0xf6`) sehingga kita akan return ke fungsi `win`.

# Flag

JOINTS21{0ff_by_On3_ez_pz_3h?}
