#!/bin/sh
docker build --tag=bon-nie-appetit .
docker run -it -p 1337:1337 --rm --name=bon-nie-appetit bon-nie-appetit