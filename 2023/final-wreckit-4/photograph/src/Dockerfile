FROM --platform=linux/amd64 python:3.11-slim-buster

ARG PASSWORD

RUN apt-get update && apt-get install -y openssh-server libcairo2

RUN mkdir /src
COPY . /src

RUN pip3 install -r /src/requirements.txt
RUN pip3 install pydantic[dotenv] python-multipart
RUN pip3 uninstall psycopg2-binary -y
RUN apt update -y && apt install -y build-essential libpq-dev
RUN pip3 install psycopg2

RUN echo root:${PASSWORD} | chpasswd
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN service ssh start

WORKDIR /src
EXPOSE 1337
EXPOSE 22

CMD /bin/bash /src/start.sh