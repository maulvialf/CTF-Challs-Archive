FROM php:8.1.10-alpine3.16

# Install system packages
RUN apk add --no-cache --update supervisor redis gcc libc-dev zip curl apache2 nginx \
    php81-apache2 php81-redis php81-json php81-phar php81-iconv php81-mbstring \
    php81-sqlite3 php81-pdo_sqlite php81-xml php81-tokenizer php81-session \
    openssl php81-openssl php81-ctype php81-dom  php81-curl php81-gd sqlite shadow

# Download composer
RUN wget https://getcomposer.org/composer-2.phar -O /usr/local/bin/composer && chmod +x /usr/local/bin/composer

# Copy configuration files
COPY config/supervisord.conf /etc/supervisord.conf
COPY config/nginx.conf /etc/nginx/nginx.conf
COPY config/proxy.conf /etc/nginx/conf.d/proxy.conf
COPY config/httpd.conf /etc/apache2/httpd.conf
COPY config/redis.conf /etc/redis.conf

# Copy App
COPY challenge /www

# Switch working environment
WORKDIR /www

# Copy flag
COPY flag /root/flag

# Add readflag binary
COPY config/readflag.c /
RUN gcc -o /readflag /readflag.c && chmod 4755 /readflag && rm /readflag.c

# Install dependencies
RUN php /usr/local/bin/composer dump-autoload
RUN php /usr/local/bin/composer install
COPY challenge/.env /www/

# Migrate DB
RUN sqlite3 /www/var/app.db ".read /www/migrations/db.sql"

# Copy symfony messenger worker
COPY --chown=root config/worker.sh /worker.sh
RUN chmod +x /worker.sh

# Set permissions
RUN chown -R apache:apache /www/var /www/vendor /www/public/static/exports
RUN usermod -g www-data redis

# Expose the port application is reachable on
EXPOSE 80

# Run supervisord
CMD /usr/bin/supervisord -c /etc/supervisord.conf
