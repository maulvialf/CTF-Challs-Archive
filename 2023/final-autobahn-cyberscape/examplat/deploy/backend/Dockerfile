FROM python:3.9-alpine

ARG PASSWORD

RUN apk add --no-cache openrc openssh 
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
RUN rc-update add sshd && rc-status && touch /run/openrc/softlevel && rc-service sshd start

RUN adduser ctf --disabled-password
RUN echo root:${PASSWORD} | chpasswd

COPY ./src/entrypoint.sh /entrypoint.sh
COPY ./src/requirements.txt /requirements.txt
COPY ./src/app /app
COPY ./src/migrations /migrations

RUN pip3 install -r /requirements.txt

RUN chmod 755 /entrypoint.sh
RUN chmod 755 -R /app

RUN mkdir /app/upload

COPY ./sample/example.yml /app/upload/example.yml

RUN chown ctf:ctf /app /app/upload /app/database.db
RUN chmod -R 777 /app/upload /app/database.db

WORKDIR /
EXPOSE 80 22
ENTRYPOINT ["./entrypoint.sh"]
