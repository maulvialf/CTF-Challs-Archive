# Courier [500 pts]

**Category:** embedded
**Solves:** 3

## Description
>b"<p>Author: <code>Addison</code></p><p>Special delivery! This device emulates a delivery system, but we dont have the ability to connect to the stampingdevice. Can you trick the target into leaking the flag?</p><p>Connections to the SNI <code>courier</code> will connect you to the UART of the device. You can test with the provided files (just install Rust with the <code>thumbv7m-none-eabi</code> target). Weve provided the <code>sender/</code> implementation as a reference.</p><p>Hint: There are very few comments. The ones that are present are extremely relevant to the intended solution.</p>\r\n\r\nNOTE: `sender` is designed to only work locally on port 42069. To communicate with the remote server, use `solver-template.py`, or run `socat -d -d  TCP-LISTEN:42069,reuseaddr,fork EXEC:openssl s_client -connect tamuctf.com\\:443 -servername courier -quiet\r\n` in a separate terminal window before running your solution."

**Hint**
* Some contestants are having issues with local builds of courier (the program issues a hard fault when executed in `qemu-system-arm`) due to a local build environment issue. We are unfortunately unable to reproduce and diagnose this issue, so we have provided a working build, but these are **not the same binaries that are on the remote server**. Notably, stamp.key and flag.txt have been replaced.\n\nIn addition, we provide the additional following hint: connections to the server will not be able to observe debug output as it is not provided over the UART connection. Therefore, to observe debug statements, you must execute it locally with the provided challenge files. You may run it locally with `make build` and `HPORTS=42069 make -e run`.

## Solution

### Flag

