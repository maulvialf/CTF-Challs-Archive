# Desc

Who doesn't love chicken?

# Note untuk panitia

- isi folder `attachement` diberikank kepada peserta
- port chal: `22223`
- buat run, masuk ke folder source, terus `docker-compose up -d`

# Flow singkat solver

Recon:

- Terdapat format string vulnerability
- Terdapat double free vulnerability

Soal heap standard (relatif lebih mudah). Leak libc dengan vuln format string, leak heap dengan vuln double free. Lalu atur heap agar mereturn address `__malloc_hook` saat kita melakukan `malloc`. Overwrite `__malloc_hook` dengan address `one_gadget`. Lakukan `malloc` agar mentrigger `one_gadget`.

# Flag

JOINTS21{ju5t_ab0uT_3verY0ne_lov3s_hie4p}
