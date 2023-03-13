#!/bin/sh
service sshd restart
su ctf && gunicorn --chdir app app:app -w 5 --threads 5 -b 0.0.0.0:80