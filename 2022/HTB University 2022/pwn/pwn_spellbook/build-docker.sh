#!/bin/sh
docker build --tag=spellbook .
docker run -it -p 1337:1337 --rm --name=spellbook spellbook