#!/usr/bin/env python3
import subprocess
import re
import sys

print("Solving the challenge doesn't require opening a PR on the official repo. Please don't do it as it might spam the ohmyzsh authors. Thanks!")
commit = input("Commit: ")
if not re.match(r'^[a-f0-9]{40}$', commit):
    print("Invalid commit")
    exit(1)

command = f'curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/{commit}/tools/install.sh | zsh'
print(command, flush=True)
subprocess.run(command, shell=True, stdout=sys.stdout, stderr=sys.stderr)
