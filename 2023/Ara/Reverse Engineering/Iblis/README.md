# Iblis [500 pts]

**Category:** Reverse Engineering
**Solves:** 0

## Description
>Polymorphic concept is insane enough for an analyst so I decided
to create **Metamorphic** concept using Zydis (https://zydis.re/).
Now no decompilers, debuggers, and disassemblers shall stand out to my masterpiece, or are there?

Note: There might be a slight bug in the challenge that there's a misused register for the input.
You only need to take a peek on the indexed register once you are able to deobfuscate or 
understand the flow of the program. Each solution is **unique** but
the binary only accepts one correct input, so I add a remote netcat service for those unique
solutions. Once you got it correctly to fulfill the condition, you will get the flag and **it's mandatory
to submit it to the remote service** instead to the binary. 

[Attachments](https://drive.google.com/file/d/1K7yh8aNSEF1deZYyivZEayQBw8WVQ00T/view?usp=sharing)

#1🩸 + Proper POC-> Bounty from the Author

Author: aseng#2055

## Service
nc 103.152.242.116 13704

#### Hint
* This binary used anti-analysis approach, but sadly the dev doesn't care about something related to the disclosed PE components. Use that for understanding the CF!

## Solution

## Flag

