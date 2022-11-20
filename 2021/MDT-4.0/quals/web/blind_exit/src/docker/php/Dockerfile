FROM php:7.4.3-fpm-alpine3.11

RUN apk add --no-cache perl
RUN apk add --no-cache exiftool
COPY ./docker/php/php-fpm.conf /usr/local/etc/php-fpm.d/www.conf
COPY ./docker/php/add.ini /usr/local/etc/php/conf.d/docker-php-ext-sodium.ini
COPY . /app


RUN rm /usr/bin/nc
RUN echo -n "MDT4.0{imagine_pwning_large_company_only_by_using_exiftool}" > /flaglab.txt
RUN chown -R root:root /app
RUN chmod 777 /app/public/uploads
