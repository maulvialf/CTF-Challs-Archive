#!/usr/bin/env python3
BLACKLISTED_CHARACTERS = "!\"#$%&',.;<>?@[\]^_`{|}~ \t\n\r\x0b\x0c"

print(open("txt/banner.txt").read())

while True:
    ask = input(">>> ").strip()
    assert len(ask) <= 36
    if not ask: continue

    for c in ask:
        if c in BLACKLISTED_CHARACTERS:
            print("Forbidden character found! Exiting...")
            exit()

    ans = eval(ask)
    assert type(ans) == float or type(ans) == int
    print(ans)
