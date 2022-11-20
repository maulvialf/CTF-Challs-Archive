FROM python:2-alpine

EXPOSE 5000

RUN apk --update add socat

WORKDIR /challs
COPY src /challs/
COPY flag.txt /secret_flag

# Securing files
RUN chown -R root:root /challs/

# Securing environ
RUN chmod 700 /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /bin/sh /usr/bin/nc /bin/cat /usr/bin/wget /usr/bin/groups /usr/bin/id /bin/ls /usr/bin/vi

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/challs/jail.py,su=nobody