FROM golang

ARG PASSWORD

RUN echo root:${PASSWORD} | chpasswd
RUN apt-get update && apt-get install -y openssh-server
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN service ssh start

WORKDIR /app/src
COPY ./src/go.mod ./
COPY ./src/go.sum ./
RUN go mod download

COPY ./src ./

RUN chmod +x /app/src/*.sh

EXPOSE 3000 22

ENTRYPOINT [ "/bin/sh", "-c", "/app/src/start.sh"]