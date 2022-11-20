FROM php:7.4.3-fpm-alpine3.11

# Copy the php config file
COPY ./docker/php/php-fpm.conf /usr/local/etc/php-fpm.d/www.conf
COPY ./docker/php/add.ini /usr/local/etc/php/conf.d/docker-php-ext-sodium.ini

# Copy the application code
COPY . /app

RUN chown -R root:root /app

VOLUME ["/app"]
