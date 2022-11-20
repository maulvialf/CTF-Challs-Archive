#!/usr/bin/env python3
from pwn import *


if __name__ == "__main__":
    # ah yes. the smell of shit code
    try:
        r = remote(args.HOST, int(args.PORT), level="warn")
        r.send("console.log('test');\nEOF\n")
        assert(r.recvline(0) == b"test")
        status = 0
        r.close()
    except AssertionError:
        status = 1
        r.close()
    except:
        status = 2
    exit(status)


