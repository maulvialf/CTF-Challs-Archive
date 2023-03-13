FROM python:3.11-slim-buster

ARG PASSWORD

WORKDIR /opt

RUN apt-get update
RUN apt-get install -y nano openssh-server socat

RUN echo root:${PASSWORD} | chpasswd
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN service ssh start

COPY server.py .

EXPOSE 18000
EXPOSE 22

RUN chmod +x server.py
CMD socat TCP-LISTEN:18000,fork,reuseaddr EXEC:'timeout 60 ./server.py'
