#!/bin/bash

/usr/sbin/sshd -D &
python3 -m uvicorn main:app --reload --port 1337 --host 0.0.0.0