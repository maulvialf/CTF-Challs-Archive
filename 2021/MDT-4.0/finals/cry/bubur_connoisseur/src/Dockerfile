FROM ubuntu:20.04

EXPOSE 5000

RUN apt-get update && apt-get -y upgrade
RUN apt-get install nano socat python3 python3-pip -y
RUN pip install pycryptodome

RUN mkdir /challs
COPY server.py /challs/server.py
COPY flag.txt /challs/flag.txt
WORKDIR /challs

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:/challs/server.py,su=nobody

# docker build -t 'bubur' .
# docker run -p 30001:5000 -itd bubur
