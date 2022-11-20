FROM ruby:2.7.2

RUN adduser -u 1001 --shell /bin/bash joints
RUN mkdir /home/joints/app

EXPOSE 3000

COPY  myapp/ /home/joints/app
WORKDIR /home/joints/app

ONBUILD RUN bundle install

RUN apt-get update -y
RUN apt-get install -y nodejs --no-install-recommends
RUN apt-get update -y
RUN apt-get install -y sqlite3
RUN gem install rails bundler
RUN bundle install
RUN apt-get install npm -y
RUN npm install --global yarn
RUN yarn install

RUN chgrp -R joints /home/joints/app
RUN chmod -R g+w /home/joints/app
RUN chmod 644 /home/joints/app/config/master.key
USER joints

CMD bin/rails server -e production
