# Use ubuntu 20.04
FROM ubuntu:20.04

# Open port 5000
EXPOSE 5000

# update
RUN apt-get update

# install socat
RUN apt-get install socat wget -y

# Set WorkDir
RUN mkdir /CTF
WORKDIR /CTF

# Copy binary to workdir
COPY flag.txt /CTF/flag.txt
COPY TryCallMe /CTF/TryCallMe

RUN chown root:root TryCallMe flag.txt
RUN chmod 755 TryCallMe flag.txt

# Securing Environment
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /bin/dash /bin/sh /bin/cat /usr/bin/id /bin/ls

# Run Program
CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./TryCallMe,su=nobody
