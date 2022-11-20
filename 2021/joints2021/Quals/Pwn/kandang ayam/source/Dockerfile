# docker build . -t joints2021-pwn3
# docker run --rm -it -p 0.0.0.0:22223:5000 --name joints2021-pwn3 joints2021-pwn3
FROM ubuntu:18.04
EXPOSE 5000
RUN apt-get update
RUN apt-get install socat wget -y
RUN mkdir /app
WORKDIR /app
COPY flag.txt /app/flag.txt
COPY chal /app
COPY libc-2.27.so /app
COPY exec.sh /app
RUN chown root:root flag.txt
RUN chmod 755 chal exec.sh
RUN chmod 444 flag.txt
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /bin/dash /bin/sh /bin/cat /usr/bin/id /bin/ls
CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/app/exec.sh,su=nobody