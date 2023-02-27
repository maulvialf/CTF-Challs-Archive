# Leakages [500 pts]

**Category:** Forensic
**Solves:** 2

## Description
>Our security team receives a notification that our website has been compromised. Upon investigation, it was discovered that an attacker had been able to leak some confidential information from our database. Could you figure it out?

[Attachments](https://drive.google.com/file/d/1SMpGen3k6svYvqUz1Ahrm_FKZJtdThlL/view?usp=sharing)

Author: fuyuka#0233

#### Hint
* After inspection, it was confirmed that the perpetrator was one of our 
users. Consequently, it was easy to locate and track down the traffic 
since it was all forwarded using our internal `transparent-proxy`.
* Our application had a bug in File Upload form. It tooks a ZipFile & extract each of the file records to a certain directory with the filename stored in a database. Due to the lack of proper mitigation, the attacker exploited it in order to leak the information insides.

A bit peculiar, but the attacker tried to leak the information one character at a time by assigning a random filename for any True/False query, so that the filename itself will be reflected on User Homepage. He also used some difference accounts during this process

## Solution

## Flag

