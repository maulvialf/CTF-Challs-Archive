## Judul Soal
Git is Fun?

## Deskripsi Soal
> In a certain place, there's an old thing. At first, there's nothing special about it. But, if you look deep enough, you'll eventually find a time machine that brings you back to a certain moment.

## Hint Soal
- RFC 1813

---

## Penjelasan Penyelesaian Soal

Diberikan berkas `history.tar.gz` yang memuat *network packet* `history.pcap`. Sebagaimana *network packet* lainnya, terlebih dahulu kita lakukan enumerasi informasi terkait hierarchy paket

<br>

**Packet Enumeration**

```bash
❯ tshark -r history.pcap -q -z io,phs                                                                                             

===================================================================
Protocol Hierarchy Statistics
Filter: 

eth                                      frames:2322 bytes:405320
  ip                                     frames:2322 bytes:405320
    udp                                  frames:2311 bytes:388666
      rpc                                frames:2300 bytes:387148
        nfs                              frames:2300 bytes:387148
      data                               frames:11 bytes:1518
    data                                 frames:11 bytes:16654
===================================================================

```

```
❯ tshark -r history.pcap | head                                                                                                   
    1   0.000000 192.168.0.110 → 192.168.0.101 NFS 206 V2 GETATTR Call, FH: 0x4e20edbb
    2   0.000262 192.168.0.101 → 192.168.0.110 NFS 138 V2 GETATTR Reply (Call In 1)
    3   0.016342 192.168.0.110 → 192.168.0.101 NFS 222 V2 LOOKUP Call, DH: 0x4e20edbb/commondir
    4   0.016551 192.168.0.101 → 192.168.0.110 NFS 70 V2 LOOKUP Reply (Call In 3) Error: NFS2ERR_NOENT
    5   0.030428 192.168.0.110 → 192.168.0.101 NFS 206 V2 GETATTR Call, FH: 0x4e20edbb
    6   0.030664 192.168.0.101 → 192.168.0.110 NFS 138 V2 GETATTR Reply (Call In 5)
    7   0.043460 192.168.0.110 → 192.168.0.101 NFS 218 V2 LOOKUP Call, DH: 0x4e20edbb/config
    8   0.043690 192.168.0.101 → 192.168.0.110 NFS 70 V2 LOOKUP Reply (Call In 7) Error: NFS2ERR_NOENT
    9   0.047954 192.168.0.110 → 192.168.0.101 NFS 218 V2 LOOKUP Call, DH: 0x4e20edbb/config
   10   0.048224 192.168.0.101 → 192.168.0.110 NFS 70 V2 LOOKUP Reply (Call In 9) Error: NFS2ERR_NOENT

```

Hasilnya, kita menjumpai sekumpulan UDP packet dengan spesifikasi `NFS-v2`. Setelah beberapa saat melakukan observasi, diketahui pula bahwa terjadi `data transfer` antara `client-server` yang melibatkan berkas `Github Repository`.

<br>

**Directory & File reconstruction**

Berdasarkan pemahaman sebelumnya, disini kita akan melakukan skema rekonstruksi `directory` beserta `file` Github Repository sesuai dengan spesifikasi yang tertera pada dokumentasi [NFS](https://tools.ietf.org/html/rfc1813).

Berikut merupakan `brief history`yang dihasilkan dari eksekusi `nfs-parser.py`

```bash
❯ python2 nfs-parser.py history.pcap | head                                                                                       
[+] Initialize git directory
[~] Creating File git/description
[v] Writing git/description
[+] Creating branches directory
[+] Creating hooks directory
[~] Creating File git/hooks/pre-applypatch.sample
[v] Writing git/hooks/pre-applypatch.sample
[~] Creating File git/hooks/prepare-commit-msg.sample
[~] Creating File git/hooks/applypatch-msg.sample
[v] Writing git/hooks/applypatch-msg.sample

```

Adapun berikut adalah Github Repository hasil rekonstruksi:

```bash
❯ tree git -L 1                                                                                                                   
git
├── branches
├── config
├── config.lock
├── description
├── HEAD
├── HEAD.lock
├── hooks
├── info
├── objects
└── refs
```

Berdasarkan informasi yang telah diperoleh sebelumnya, kita dapat menyimpulkan bahwa repository yang diperoleh merupakan `Bare Repository` dari sebuah Git Server.

Dari sini, kita perlu mengubahnya menjadi `Normal repository` untuk dapat mengakses VCS management sebagaimana Github Repository pada umumnya.

```bash
❯ mkdir normal-repo
❯ mv git normal-repo/.git
❯ cd normal-repo
❯ rm -rf .git/*.lock
❯ git config --local --bool core.bare false 

❯ git log --oneline | head 

e8fe334 Flag character: 79th index
91adade Flag character: 78th index
4eb9433 Flag character: 77th index
b2e1855 Flag character: 76th index
ef0d646 Flag character: 75th index
3380709 Flag character: 74th index
4ea7f07 Flag character: 73th index
24b1685 Flag character: 72th index
1d73f49 Flag character: 71th index
065c969 Flag character: 70th index

```

<br>

**Information Retrieval**

Sesaat setelah mendapatkan akses VCS dari `normal repository`, kita menjumpai berapa `commit` yang berisikan `character index` dari berkas `entitas flag` sebanyak 1 karakter.

Terakhir, menggunakan script berikut akan dilakukan proses pemetaan informasi dari `flag.txt`. Hasilnya diperoleh informasi flag sebagaimana berikut init:

```python
# commit-map.py
import os

def read_file(name):
    with open(name, 'rb') as handle:
        return handle.read().decode()

logs = os.popen('cd normal-repo && git log --oneline').readlines()
result = dict()

for log in logs[::-1]:
    commit_id = log.split()[0]
    index = log.split()[-2][:-2]
    os.popen('cd normal-repo && git checkout ' + commit_id)
    content = read_file('normal-repo/flag.txt')
    result[int(index)] = content

print(''.join(result.values()))

```

```bash
❯ cd ..
❯ python2 commit-map.py

redmask{n3ver_us3_netw0rk_f1l3_sy5tem_for_vcs_rep0s1tory_m4nagem3nt_6de31dfbd3}
```

<br>

## Flag

redmask{n3ver_us3_netw0rk_f1l3_sy5tem_for_vcs_rep0s1tory_m4nagem3nt_6de31dfbd3}
