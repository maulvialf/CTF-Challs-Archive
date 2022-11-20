FROM php:7.3-fpm

# Copy composer.lock and composer.json
COPY ./app/composer.lock /var/www/
COPY ./app/composer.json /var/www/

# Set working directory
WORKDIR /var/www

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    locales \
    zip \
    vim \
    unzip \
    git \
    zlib1g-dev \
    libzip-dev \
    libsqlite3-dev \
    curl

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install extensions
RUN docker-php-ext-install pdo_mysql pdo_sqlite mbstring zip exif pcntl

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# # Add user for laravel application
# RUN groupadd -g 1000 www
# RUN useradd -u 1000 -ms /bin/bash -g www www

# Copy existing application directory contents
COPY ./app /var/www

ENV APP_NAME=WTube \
    APP_KEY=base64:xxWiZdc+32XZyLChIiLFals7XwglYh2kyQzm+bFIUg4= \
    APP_ENV=local \
    DB_CONNECTION=mysql \
    DB_HOST=202.148.27.84 \
    DB_PORT=17013 \
    DB_DATABASE=wtube \
    DB_USERNAME=Bambang123@ \
    DB_PASSWORD=Bambang123@ \
    MAIL_MAILER=mailgun \
    MAIL_HOST=smtp.mailgun.org \
    MAIL_PORT=587 \
    MAIL_USERNAME=bambang@mail.cacadosman.com \
    MAIL_PASSWORD=502e616f0cb2d821b89979bddc6e1307-360a0b2c-d087f1d9 \
    MAIL_ENCRYPTION=tls \
    MAIL_FROM_ADDRESS=wtube@mail.cacadosman.com \
    MAIL_FROM_NAME=WTube \
    MAILGUN_DOMAIN=mail.cacadosman.com \
    MAILGUN_SECRET=79bf6dd42b830d36afdce112ad8602c7-360a0b2c-53b4f490

RUN cd /var/www && composer install && php artisan migrate:fresh

# # Copy existing application directory permissions
RUN chmod -R 777 /var/www/
# COPY --chown=www:www . /var/www
# RUN chmod -R 777 /var/www/storage/*
# FAK INI KENAPA UDH CHMOD 777 TETEP PERMISSION DENIED DATABASENYA
# RUN chmod -R 777 /var/www/database/database.sqlite

# # Change current user to www
# USER www

# Expose port 9000 and start php-fpm server
EXPOSE 9000
CMD ["php-fpm"]
