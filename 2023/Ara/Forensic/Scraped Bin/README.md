# Scraped Bin [500 pts]

**Category:** Forensic
**Solves:** 2

## Description
>One day, I went to a thrift store and unconsciously bought an antique item. The merchant said that it was made in a peculiar way, so the insides might be particularly irrelevant. It was also secured by a passphrase, but it seems to be weak. Unfortunately, it was missing some parts, thus making it unreadable

[Attachments](https://drive.google.com/file/d/1X4-XYl349gXIHvr_Ajt5OOil1c519TOE/view?usp=sharing)

Author: fuyuka#0233

#### Hint
* It was tampered with, but not particularly corrupted. Consequently, it may affect on how the file records are gonna be listed and extracted to your file system. Furthermore, you may look for the ZIP appnote / documentation
* You may go with either full restoration of `Central File Header` with proper filename or directly extract the `datastream`
* Here's a piece of trivia: did you know that a ZipFile cannot be extracted if there is a file record with a `filename` length that exceeds 260 characters? However, the length may vary depending on the software and operating system you use

## Solution

## Flag

