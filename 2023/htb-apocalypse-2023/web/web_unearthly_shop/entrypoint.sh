#!/bin/bash

# Secure entrypoint
chmod 600 /entrypoint.sh

# Start mongodb
mkdir /tmp/mongodb
mongod --noauth --dbpath /tmp/mongodb/ &

# Wait for mongodb
while ! mongostat --discover -n1 --quiet; do echo "not up"; done

# Secure admin account
PASSWORD=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 16 | head -n 1)
sed -i "s/\[REDACTED\]/${PASSWORD}/g" /opt/schema/users.json

# Import collections
mongoimport --db unearthly_shop --collection users --file /opt/schema/users.json --jsonArray
mongoimport --db unearthly_shop --collection products --file /opt/schema/products.json --jsonArray
mongoimport --db unearthly_shop --collection orders --file /opt/schema/orders.json --jsonArray

/usr/bin/supervisord -c /etc/supervisord.conf