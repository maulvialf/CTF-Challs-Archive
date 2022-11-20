FROM ubuntu:16.04
EXPOSE 5000
RUN apt-get update
RUN apt-get install socat wget -y
RUN mkdir /app
WORKDIR /app
COPY flag.txt /app/flag.txt
COPY main /app/main
RUN chown root:root flag.txt
RUN chmod 755 main
RUN chmod 444 flag.txt
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /bin/dash /bin/sh /bin/cat /usr/bin/id /bin/ls
CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./main,su=nobody
