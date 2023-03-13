FROM --platform=linux/amd64 python:3.11-slim-buster

ARG PASSWORD

RUN apt-get update

RUN mkdir /src
COPY . /src

RUN pip3 install -r /src/requirements.txt
RUN pip install pydantic[dotenv]
RUN pip3 install python-multipart
RUN pip uninstall psycopg2-binary -y
RUN apt update -y && apt install -y build-essential libpq-dev
RUN apt-get install -y openssh-server
RUN pip install psycopg2

RUN echo root:${PASSWORD} | chpasswd
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN service ssh start

WORKDIR /src
EXPOSE 1337
EXPOSE 22
RUN chmod +x start.sh
CMD ./start.sh