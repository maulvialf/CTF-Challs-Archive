# Steg as a Service [500 pts]

**Category:** BIN-PWN
**Solves:** 2

## Description
>Made by MetaCTF\r\n<p>Welcome to the cyberlabs, where we perform threat hunting on various threat actors to track their activities. Our prized utility of choice is a service that we provide, called Steg as a service. <s>Since all the 1337 threat actors use steghide to exfiltrate data,</s> This service allows anyone to upload a file to see if steghide can find any hidden information inside it. <br><br>\r\nUnfortunately,  we\ve recently discovered that we got our copies of steghide from a shady source, and our team has discovered and patched a sneaky backdoor inside it!!! However, since the backdoored version of steghide doesn\t trigger any antivirus detections, we\ve been having trouble convincing our managers to change the version of steghide into a secure one.  Can you try exploiting our shady copy of steghide so that we can convince our managers to update the binary? <br><br>\r\n\r\nWe\ve spun up a copy of our Steg service at <a href="http://host1.metaproblems.com:5830">http://host1.metaproblems.com:5830</a> for you to target. If you want a local setup, this <a href="https://metaproblems.com/769829afb2a31c32e153cc53484f346a/steg.zip" target="_blank">docker container</a> should do the trick. Unfortunately, our team member who discovered the backdoor is currently on PTO, so I can\t provide you with the exact details on what the backdoor was. However, I could give you our <a href="https://metaproblems.com/769829afb2a31c32e153cc53484f346a/steghide-patched" target="_blank">patched steghide</a> if it helps.\r\n<br><br><b>Note:</b> Although this is hosted as a web service, the intended vulnerability is within the steghide binary, not the web service.</p>\r\n\r\nNOTE: This flag\s format is MetaCTF{}

**Hint**
* -

## Solution

### Flag

