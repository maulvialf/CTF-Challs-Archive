## Judul Soal
RaaS

## Deskripsi Soal

> Introducing `Recyler as a Service (RaaS)`, an utility to track your projects in a fun way.
---

## Hint
- The service used custom `Gitserver hooks` to trigger a certain event 

---
## Proof of Concept

- From a given pcap, we get a bunch of `NFSv4` packets
- By mapping NFSv4 command with NFSv4 data, we managed to reconstruct each of `transferred files`
-  Here we found several files/directory with `Df` prefix. Also we found an `INFO2` file

    ```
    $ tree  | head
    .
    └── S-1-5-21-4120123742-30011560200-102401200-1001
        ├── Df1
        ├── Df10
        ├── Df100
        ├── Df1000
        ├── Df1001
        ├── Df1002
        ├── Df1003
        ├── Df1004

    ```

- We can conclude that the services used `Recyler implementation` which is introduced in Windows XP
- From here, simply mapping each of `Indexed-number` with `original_path` insided `INFO2` file

    ```
    $rifiuti INFO2 | head
    Recycle bin path: 'INFO2'
    Version: 5
    OS Guess: Windows XP or 2003
    Time zone: UTC [+0000]

    Index	Deleted Time	Gone?	Size	Path
    1	2021-04-05 20:15:28	No	66	f:\project.git\config
    2	2021-04-05 20:15:28	No	73	f:\project.git\description
    3	2021-04-05 20:15:28	No	23	f:\project.git\HEAD
    4	2021-04-05 20:15:28	No	424	f:\project.git\hooks\pre-applypatch.sample

    ```
- After we managed to recover the Git repository, simply grab `password.txt` from each `Git branch` & concate it as a `password` for `flag.zip`

## Flag
JOINTS21{4_n0stalgic_bouqu3t_from_2001_computer_3ra} 

