# PwnDroid [500 pts]

**Category:** Reverse Engineering
**Solves:** 0

## Description
>Another real-world bad mobile dev perspective so he got an unbreakable Schrödinger-cryptic puzzle APK.  Give me the secrets!

[Attachments](https://drive.google.com/file/d/1SiTiytCKWqO_p1LiBi7fpBVo5BnEIoHO/view?usp=sharing)

#1🩸 + Proper POC-> Bounty from the Author

Author: aseng#2055

#### Hint
* This bad developer forgets to enable a crucial gradle properties when building this APK :( Punish him by getting the secrets!
* Crypto/Misc is not a spice in here,you need to leverage an **unknown** vulnerability which is related to that. Bruteforce is not the only option for one of the crypto attributes there, it really does exist but maybe you haven't figured it out yet! Perhaps what needs to be done is by inspecting the known factors to reveal the unknown.
* There are packages which are used inside the APK, one of them is pretty unique to be analyzed. Although **one** of the attribute is said to be **secured**, yet it actually doesn't. What would you interpret a "**waste**" from a really-secure package's function? This might indicates either one of the core components are pretty much to be produced easily once **you recreate** it especially in **Dart**.

## Solution

## Flag

