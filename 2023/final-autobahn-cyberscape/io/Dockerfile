FROM rust:latest
WORKDIR /usr/src/io
ARG PASSWORD

# SSH SETUP
RUN echo root:${PASSWORD} | chpasswd
RUN apt-get update && apt-get install -y openssh-server
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN service ssh start

COPY src ./src
COPY Cargo.toml .
COPY Cargo.lock .
COPY start.sh .

RUN cargo build --release

EXPOSE 10000
EXPOSE 22

RUN chmod +x ./start.sh
CMD ./start.sh