# First Responder [500 pts]

**Category:** rev
**Solves:** 8

## Description
>b"<p>Author: <code>Mr. Blade</code></p><p>One of our client companies was recently hit with a cyber attack. During the initial investigation by our incident responders, a recently modified sshd binary was discovered.</p><p>Can you check if the attackers installed a backdoor in sshd?</p><p>Note: The username you need to use is <code>billy</code>.</p>\r\n\r\nOnce you have the correct password, SSH to `tamuctf.com` with the SNI `first-responder `. \r\n\r\nTo do this, run `socat -d TCP-LISTEN:4444,reuseaddr,fork EXEC:openssl s_client -connect tamuctf.com\\:443 -servername first-responder -quiet`; this will appear to hang. In a separate terminal, run `ssh billy@localhost -p 4444`, then put in the password."

**Hint**
* -

## Solution

### Flag

