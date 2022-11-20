FROM node:12

# Create app directory
WORKDIR /app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY ./app /app

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

RUN groupadd -g 999 www
RUN useradd -u 999 -ms /bin/bash -g www www

USER www

EXPOSE 3000
CMD [ "node", "index.js" ]
