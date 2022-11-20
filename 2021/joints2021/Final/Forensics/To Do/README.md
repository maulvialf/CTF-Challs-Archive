## Judul Soal
To Do

## Deskripsi Soal

> I often forgot about my daily task. Since then, I created a To Do list webservice in order to list & manage my own TODO. <br><br> Unfortunately, It has a big flaws, so that I decided to discontinue this project.
---

## Hint
- I made some [patches](https://gist.github.com/hanasuru/b333e3d655f6046a3aade480c284ce07) before I discontinue this project.
- Despite having some flaws, I managed to encrypt my data, so that it can only be decrypted if you have access to its original `source code`.

---
## Proof of Concept

- From given pcap get a bunch of TLS & TCP-Socket packet, filter on TCP-socket got sslkeylogfile
- Decrypt TLS packet using sslkeylogfile, then got HTTP/2 packet
- From HTTP/2 packet, there're bunch of add/edit task requests. Furthermore, there're also SQLi attempt
- Everytime a new PDF was generated, there're an addition of Embedded object. Based on, attack payload we can conclude that there's LFI vulnerability based on WeasyPrint
- By mapping order of filename & its Embedded object, we recovered each of .bzr files
- After successfully retrieved the whole files, revert the .bzr repository to its latest commit
- From recovered repository, we got a set of Docker configuration + an encrypted directory `web`
- If we look up further, we can see `EncFS` command that took a part in `/app` decryption
- Using `PASSWD` we got from `/proc/self/environ`, we can decrypt `EncFS` manually on a localhost or build it using docker-compose
- There's a `AES helper` which adds Encryption and Decryption support to the `Task description`
- From there just look up into `group_concat(description) whered id=1` query to obtain all of encrypted `admin notes`.
- Using provided `helper function`, we obtained `admin notes`

```
1. Fwaaaah. I feel dizzy. Maybe it&#x27;s time to go to bed..
2. Hmm ... Sleeping twice is the best, isn&#x27;t it? That&#x27;s why good night
3. Err... I have something for you, but I don&#x27; think it can be written here
4. Ah, my bad. I forgot to bring it. Wait a moment, I&#x27;ll back as soon as possible
5. https://drive.google.com/file/d/1Cb1_9YhUsLQRd-EX0__R_T6awxD2YbxR/view?usp=sharing
6. I hope you like my gift
7. Well then, I&#x27;ll back to sleep I guess. Oyasumi~
```

## Flag
JOINTS21{4lways_b3w4re_of_exp0s3d_vcs_even_it5_canonical_0ne} 

