#!/bin/bash

docker build . -t misc_calibrator
docker run --rm -it --name misc_calibrator -p1337:1337 misc_calibrator
