# Desc

This program can save your custom bytecode and run it (maybe). But it still under development so there're some bugs.

# Note untuk panitia

- Versi OS adalah Ubuntu 20.04
- Peserta diberikan binary yang sudah dicompile (bytecode_runner) dan file libc (libc.so) di folder attachment

# Flow singkat solver

Terdapat buffer overflow di fugsi read_str dimana jika size input 0 maka fungsi akan meletakkan nilai 0 di buf\[255\]. Kita dapat memanfaatkan vuln tersebut untuk memakai teknik house of einherjar dengan mengoverwrite prev_inuse bit. Pemakaian teknik ini bertujuan untuk mengoverwrite fd pointer chunk yang di-overlap sehingga saat memanggil malloc kita dapat mengontrol address manapun. Salah satu address yang akan kita kontrol adalah __free_hook yang dapat kita manfaatkan untuk mendapatkan remote shell.

# Flag

JOINTS21{wh3n_y0u_f0rg3t_Re4d_s1z3_c4n_B3_Z3r0}