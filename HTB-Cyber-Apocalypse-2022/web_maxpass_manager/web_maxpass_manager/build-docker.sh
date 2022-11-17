#!/bin/bash
docker rm -f web_maxpass_manager
docker build -t web_maxpass_manager . 
docker run --name=web_maxpass_manager --rm -p1337:1337 -it web_maxpass_manager
