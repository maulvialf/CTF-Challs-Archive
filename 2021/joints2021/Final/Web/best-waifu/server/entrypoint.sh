#!/bin/bash

FILE=/tmp/init.php
if test -f "$FILE"; then
    sleep 5s
    php $FILE
fi

php-fpm