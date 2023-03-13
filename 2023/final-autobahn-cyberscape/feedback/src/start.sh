#!/bin/sh
service mysql restart
service ssh start
mysql -u root -e "create database fakedb"
mysql -u root fakedb < fakedb.sql
rm fakedb.sql
cd /opt/app
npm start


