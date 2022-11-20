FROM python:latest

RUN groupadd -g 666 nobodi
RUN useradd -r -u 666 -g nobodi -m nobodi

RUN pip install pycryptodome
RUN apt-get update -y
RUN apt-get install socat -y
COPY chall.py flag.txt /home/nobodi/
WORKDIR /home/nobodi
RUN chmod +x chall.py
USER nobodi

CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./chall.py
