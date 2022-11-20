FROM ubuntu:18.04

EXPOSE 5000
RUN apt update
RUN apt install socat python python-pip curl -y
RUN mkdir /app
COPY chall.py secret.py /app/
WORKDIR /app
# RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
# RUN python2 get-pip.py
RUN pip install pycrypto
RUN chmod 755 chall.py
RUN chown -R root:root /app
RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /bin/dash /bin/sh /bin/cat /usr/bin/id /bin/ls
CMD socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./chall.py
