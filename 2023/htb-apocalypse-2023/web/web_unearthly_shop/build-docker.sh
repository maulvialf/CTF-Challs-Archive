#!/bin/bash
docker build -t web_unearthly_shop .
docker run  --name=web_unearthly_shop --rm -p1337:80 -it web_unearthly_shop