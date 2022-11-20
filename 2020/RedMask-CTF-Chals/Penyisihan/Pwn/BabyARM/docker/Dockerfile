FROM ubuntu:20.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y qemu-user-static xinetd && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /root/

RUN useradd -m -s /bin/bash ctf
COPY main /home/ctf/
COPY run.sh /home/ctf/
COPY flag.txt /home/ctf/
COPY babyarm /etc/xinetd.d/

EXPOSE 1337

CMD xinetd -dontfork