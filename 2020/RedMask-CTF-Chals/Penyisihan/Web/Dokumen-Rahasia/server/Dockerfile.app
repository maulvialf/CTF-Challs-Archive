FROM php:7.4.1-apache

USER root

# Set working directory
WORKDIR /app

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
    curl

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install extensions
RUN docker-php-ext-install pdo_mysql zip

RUN echo 'redmask{waifu_untuk_kebutuhan_iman}' > /fl4g_adalah_sebuah_bendera

RUN groupadd -g 999 www
RUN useradd -u 999 -ms /bin/bash -g www www

# Copy existing application directory contents
COPY ./app /app
COPY ./vhost.conf /etc/apache2/sites-available/000-default.conf

RUN a2enmod rewrite