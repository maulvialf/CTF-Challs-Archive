# Uniwack Spooky 1108 MainFrame [300 pts]

**Category:** Programming
**Solves:** 24

## Description
><iframe src="" style="background-image: url(\https://cyberhacktics.sfo2.digitaloceanspaces.com/DEADFACECTF2022/Challenges/Images/uniwack-spooky.jpg\);background-size:contain;background-position:center center;background-origin:content-box;background-repeat:no-repeat;background-color:rgb(40, 40, 40);min-height:160px;height:160px;width:100%;padding:0px;border:none" title="Iframe Example"></iframe>\r\n\r\n<sup>Created by: <b>TheZeal0t</b></sup>\r\n\r\nWe\ve intercepted a raw dump of a communication between Codename "DarkAngel" and Dr. Charles Geschickter of Lytton Labs.  It was recovered from a Uniwack Spooky 1108 mainframe.  We don\t have access to a Spooky mainframe, since they went out of production sometime around 1966.  We were able to find some information about what we think is the raw bit format.\r\n\r\nWords are in 38-bit format: two 18-bit half words with one bit of even parity.  Bits are numbered left to right, low bit to high bit.  Each byte is nine bits.  The file should be in ASCII, so that means values 0-127 (the two most significant bits are 0\s).\r\n\r\nThe Even Parity bit is 1 if number of 1\s in the half word is even, 0 if odd.\r\n\r\n**UPDATE: THIS IS BACKWARDS.  See this article.  What I have described above is ODD Parity.  Follow my instructions above, and it will work.**\r\n\r\n[Parity Explained](https://en.wikipedia.org/wiki/Parity_bit)\r\n\r\nHalf Words found to have bad parity are automatically re-transmitted.  Therefore, if the parity for a Half Word does not match (it is incorrect), throw out that Half Word and move to the next.\r\n\r\nWORD FORMAT:\r\n[Download Word Format Diagram](https://tinyurl.com/2nybezt8)<br>\r\n<sup>SHA1: `a62c2e4dcc26317fa282b20950ede51f5cc15104`</sup>\r\n\r\nWe need you to write a program that will decode the raw file to recover the intelligence we need to uncover Codename "DarkAngel\s" nefarious plans with Dr. Geschickter.  Specifically, we need to know the name of the PROTOCOL they are initiating.\r\n\r\nEnter the flag as: `flag{XXX PROTOCOL}`. \r\n\r\n[Download Binary Dump File](https://tinyurl.com/3pkv9xjm)<br>\r\n<sup>SHA1: `7a3cb4f4bd1d409d6b7578f8f1e6248f5b536bd5`</sup>

**Hint**
* -

## Solution

### Flag

