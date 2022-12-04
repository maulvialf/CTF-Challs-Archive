FROM node:18-alpine3.15

# Install system packages
RUN apk add --update --no-cache supervisor mariadb mariadb-client gcc musl-dev \
    curl nginx chromium chromium-chromedriver

# Setup application
RUN mkdir -p /opt/exports && chown node:node /opt/exports
RUN mkdir -p /app

# Copy flag
COPY flag.txt /flag.txt

# Add application
WORKDIR /app
COPY challenge .

# Install dependencies
RUN npm install --legacy-peer-deps

# Setup superivsord
COPY config/supervisord.conf /etc/supervisord.conf
COPY config/nginx.conf /etc/nginx/nginx.conf

# Expose the port node-js is reachable on
EXPOSE 80

# Populate database and start supervisord
COPY --chown=root entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh
