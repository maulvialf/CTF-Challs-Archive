#!/bin/bash
docker build -t web_spell_orsterra .
docker run --name=web_spell_orsterra --rm -p1337:80 -it web_spell_orsterra
