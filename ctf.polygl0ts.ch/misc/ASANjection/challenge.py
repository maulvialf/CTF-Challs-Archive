#!/usr/bin/env python3
import base64
import os
import subprocess
import sys

def main():
    # Setup
    os.system("cp ./main.c /tmp")
    os.chdir("/tmp")

    # Welcome
    print("Hello there!")
    print("Let's have some compiler fun!\n", flush=True)

    # Explain
    print("Here is how it works:")
    print("1. Your input a base64 encoded string.")
    print("2. Your input is decoded and appended to `main.c`.")
    print("3. `main.c` is compiled and executed.\n", flush=True)

    # Get user input
    raw = input("base64 input: ")
    line = base64.b64decode(raw)

    # Write main.c
    with open("main.c", "ab") as f:
        f.write(line)

    # Compile main
    os.system("gcc main.c -fsanitize=address -g -o main")

    # Run main
    x = subprocess.run(["./main"], stdout=sys.stdout, stderr=subprocess.DEVNULL)

if __name__ == '__main__':
    main()
