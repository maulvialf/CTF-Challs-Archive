# Komori Met [1000 pts]

**Category:** Pwn
**Solves:** 0

## Description
>met.ko(mori) \r\n\r\nbadum tss\r\n\r\n(laugh please)\r\n\r\nAuthor: Zafirr

**Hint**
* 1. theres no difference between copy_from_user, \\_copy_from_user and raw_copy_from_user right?\n\n2. ever heard of struct pt_regs?\n* pt_regs is saved in the stack\n\noverflownya cuma 1 word, tapi kalo bisa kita ganti isi pt_regs mungkin bisa lompat kesitu....

## Solution

### Flag

