FROM nginx:alpine

# Copy existing application directory contents
COPY ./app /var/www

COPY ./nginx.conf.d /etc/nginx/conf.d/default.conf

# Set working directory
WORKDIR /var/www