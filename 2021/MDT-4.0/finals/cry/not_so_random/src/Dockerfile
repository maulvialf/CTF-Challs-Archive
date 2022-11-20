FROM ubuntu:20.04

EXPOSE 5000

RUN apt-get update && apt-get -y upgrade --fix-missing
RUN apt-get install nano socat python3 -y

RUN mkdir /challs
COPY server.py /challs/server.py
COPY flag.txt /challs/flag.txt
WORKDIR /challs

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/challs/server.py,su=nobody

# docker build -t 'notsorandom' .
# docker run -p 30002:5000 -itd notsorandom
