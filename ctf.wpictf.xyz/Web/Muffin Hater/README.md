title: Muffin Hater
value: 400
description: Muffinhater88 has encrypted your precious photos of Muffin! I found his c&c server, I have it on pretty good authority that his username is `muffinhater88`. It seems his site is designed using an old version of FastAPI (0.65.1), meaning it is possible to take advantage of this CVE: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-32677. Can you break-in to his site and recover the encryption keys?
I found a search page that may be useful, and he seems to have left his api documentation exposed at `/docs` on his C&C server. You can send him URLs at `/simulated-user`.

Main Server: http://muffin-hater.wpi-ctf-2022-codelab.kctf.cloud:8000
Search Server: http://muffin-hater.wpi-ctf-2022-codelab.kctf.cloud:8080

NOTE: No brute forcing is required for this challenge! (that means no directory scanning either!)