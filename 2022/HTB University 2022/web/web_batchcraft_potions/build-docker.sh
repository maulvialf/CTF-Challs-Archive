#!/bin/bash
docker build -t web_batchcraft_potions .
docker run --name=web_batchcraft_potions --rm -p1337:80 -it web_batchcraft_potions
