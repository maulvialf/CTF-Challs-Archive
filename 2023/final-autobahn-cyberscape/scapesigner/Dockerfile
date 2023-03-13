FROM python:3.11-slim-buster

ARG PASSWORD
ARG SCAPESIGNER_ADMIN_USERNAME
ARG SCAPESIGNER_ADMIN_PASSWORD

WORKDIR /opt

RUN apt-get update
RUN apt-get install -y nano openssh-server

RUN echo root:${PASSWORD} | chpasswd
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN service ssh start

COPY src/ .

RUN pip install -r requirements.txt
RUN python3 database/reset.py ${SCAPESIGNER_ADMIN_USERNAME} ${SCAPESIGNER_ADMIN_PASSWORD}

EXPOSE 80
EXPOSE 22

RUN chmod +x ./start.sh
CMD ./start.sh
