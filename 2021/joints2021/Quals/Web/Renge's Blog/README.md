# Renge's Blog
Web : Med-easy(mungkin)
## Deskripsi
Renge baru mencoba belajar membuat blog dari nol, bantu renge mengecheck keamanan blognya
## Note to panita
### How to deploy
1. kalo mau ganti port nya, cek `docker-compose.yml`. Ganti `45500` jadi port yang diinginkan
2. pake docker-compose. Command: `docker-compose up --build -d`

FLAG : JOINTS21{H1d3_y0ur_key5}

## How to solve
1. janlup inspect element
2. ada note mengenai public.key
3. liat halaman admin
4. forbidden -> liat cookies -> ada token(JWT)
5. Ganti JWT biar `admin:true` pake private.key di /key/private.key
6. masuk ke halaman admin


