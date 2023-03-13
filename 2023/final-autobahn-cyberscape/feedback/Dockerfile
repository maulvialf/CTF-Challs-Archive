FROM ubuntu:20.04

## for apt to be noninteractive
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN echo "tzdata tzdata/Areas select Europe" > /tmp/preseed.txt; \
    echo "tzdata tzdata/Zones/Europe select Berlin" >> /tmp/preseed.txt; \
    debconf-set-selections /tmp/preseed.txt && \
    apt-get update && \
    apt-get install -y tzdata
RUN apt-get update --fix-missing && apt-get install -y --no-install-recommends openssh-server
RUN apt-get install -y software-properties-common
RUN apt-get update
RUN apt-get install -y mysql-server mysql-client
RUN apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs
RUN apt-get install -y tar bzip2
RUN apt-get install -y libfontconfig
RUN apt-get install -y ca-certificates 

RUN rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /opt/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
# COPY package*.json /usr/src/app
COPY ./src/. .

ENV MYSQL_DATABASE=fakedb \
    MYSQL_USER=REDACTED \
    MYSQL_PASSWORD=REDACTED \
    MYSQL_ROOT_PASSWORD=REDACTED

RUN npm install
# If you are building your code for production
#RUN npm ci --only=production
RUN chmod +x start.sh

# Bundle app source
CMD [ "/bin/bash", "-c", "./start.sh" ]

EXPOSE 3000