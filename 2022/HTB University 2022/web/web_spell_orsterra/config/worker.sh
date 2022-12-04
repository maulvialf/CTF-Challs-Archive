#!/bin/ash

chmod 0700 /worker.sh

while true; do
    php81 /www/bin/console messenger:consume SendMailTransport --time-limit=60 -vv
    echo "DEL messages" | redis-cli
done