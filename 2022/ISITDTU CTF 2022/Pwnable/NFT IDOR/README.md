# NFT IDOR [500 pts]

**Category:** Pwnable
**Solves:** 0

## Description
>I heard that people can own NFT, but can we pwn NFT?\r\n\r\nSource build instruction:\r\n\r\nClone Linux kernel commit 4fe89d07dcc2804c8b562f6c7896a45643d34b2f (tag v6.0), then revert the commit 95f466d22364a33d183509629d0879885b4f547e.\r\n\r\n<a href="https://1drv.ms/u/s!An22WwPilIZ74nsXWxQsX0a4K8J4?e=vybPpz" style="color:red;">.config</a> \r\n\r\n<a href="https://1drv.ms/u/s!An22WwPilIZ74njaj6tPu3R6f_q_" style="color:red;">Compiled kernel on server</a>\r\n\r\n<a href="https://1drv.ms/u/s!An22WwPilIZ74noYC9ZAqsO3EIN6" style="color:red;">Disk image on server</a>\r\n\r\nIt will have python, vim, nano, build-essential and libnftnl-dev installed so you can build your exploit there. /tmp is writable.\r\n\r\nQEMU command line:\r\n\r\n```\r\nqemu-system-x86_64 -m 1024 -hda nft.qcow2 -nographic -smp 2 -kernel bzImage -append "root=/dev/sda ro console=ttyS0"\r\n```\r\n\r\nLogin: nft / nft\r\n\r\nNote: Please verify your exploit first before attempting on the server, as it\s very slow and you will have to wait for POW.\r\n\r\nAlso please don\t DDOS the infrastructure to create a fair competition for others!\r\n\r\n```nc 34.125.252.51 31337```\r\n\r\nOn the server, the flag will be at /flag.

**Hint**
* -

## Solution

### Flag

