# Kernelmania [500 pts]

**Category:** Forensic
**Solves:** 2

## Description
>Canada Forensic Bureau Office Analyst at ARA Corp. has just identified an infected
computer system from one of the employee who works there. 
They already knew that the `malware.exe` process with PID `2704` is the root of the cause but
they need to fill out the analytics report.

The malware itself resides in the `Desktop` folder of the victim but they need to know
the **VA (Virtual Address)** at some point. 
**When the malware file is OPENED in the system, What is the VA of the victim's device?**

Flag format: ARA2023{hexaddress}

Example: ARA2023{0xb0b4f3dddddddddd}

Download the file here: 
[Attachments](https://drive.google.com/file/d/1ovFSEhizg2gMREMgrx73fy7MM3UJM9qy/view?usp=share_link)

Password ZIP:  `ARA2023_w!th_fUyUk4_0xcafef00d`

#1🩸 + Proper POC-> Bounty from the Author (DONE to Team [GBK](https://ctf.its-ara.com/admin/teams/355))

Author: aseng#2055 & aiko#3010

#### Hint
* This requires a bit of research on Windows Driver struct which related to an OBJECT. But what kind of OBJECT is it?
* This **tutorial** helps especially for defining the mentioned object that you might look for ~

https://www.tophertimzen.com/resources/cs407/slides/week02_01-volshell.html#slide1

## Solution

## Flag

