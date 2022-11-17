#!/bin/bash
docker rm -f web_acnologia_portal
docker build --tag=web_acnologia_portal .
docker run -p 1337:1337 --rm --name=web_acnologia_portal web_acnologia_portal