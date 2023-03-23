#!/bin/bash

docker build . -t misc_bastion
docker run --rm -it --name misc_bastion -p1337:1337 misc_bastion