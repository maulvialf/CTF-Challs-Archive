title: Keepin' it Real
value: 500
description: We managed to recover an old control system, but we can't seem to figure out how to get the thing to work! Device documentation suggests that it shipped with some kind of client software that is no longer available. Luckily, we were able to recover the firmware image from a flash chip on the board. It appears to be listening on TCP port 10033.
Flag format: flag{...}
```
nc -v kir.ctf.battelle.org 10033
```
Hint: There is no prompt displayed on a successful connection, after connecting hit enter a few times to see proprietary data start to come back