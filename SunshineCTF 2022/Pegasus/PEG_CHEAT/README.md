# PEG_CHEAT [300 pts]

**Category:** Pegasus
**Solves:** 1

## Description
>b">Silicon Bridge is the classic thrilling game of chance! All you need to do is cross the bridge thats made up of two rows of silicon tiles. But be careful! At each step, one of the two silicon tiles will not support your weight! Can you make it to the end?\r\n\r\nThats what the description on this game cartridge says, but Silicon Bridge seems impossible. Maybe theres some way to cheat?\r\n\r\n=====\r\n\r\nRun locally:\r\n```\r\necho sun{fake_local_flag} > flag.txt\r\nrunpeg --plugin peg_cheat_checker.so SiliconBridge.peg [--debug] [--verbose] [--trace]\r\n```\r\n\r\nRun on the challenge server:\r\n```\r\nnc sunshinectf.games 22704\r\n```\r\n\r\nPegasus program:\r\n* [SiliconBridge.peg](https://sunshinectf.games/21478ecf6429/SiliconBridge.peg)\r\n\r\nChecker module for runpeg, just allows accessing a `flag.txt` file by reading from port 0xF (for Flag, get it?):\r\n* [peg_cheat_checker.so](https://sunshinectf.games/21478ecf6429/peg_cheat_checker.so)\r\n\r\nAuthor: kcolley"

**Hint**
* -

## Solution

### Flag

