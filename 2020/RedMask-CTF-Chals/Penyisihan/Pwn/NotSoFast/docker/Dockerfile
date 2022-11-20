FROM ubuntu:18.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y gcc make patch xz-utils xinetd && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /root/

# get quickjs
ARG QUICKJS_VERSION="2020-11-08"
ADD "https://bellard.org/quickjs/quickjs-${QUICKJS_VERSION}.tar.xz" /root/
RUN tar xf "quickjs-${QUICKJS_VERSION}.tar.xz" && rm "quickjs-${QUICKJS_VERSION}.tar.xz"

# patch build install
COPY no-system-modules.patch /root/quickjs-${QUICKJS_VERSION}
COPY how2heap.patch /root/quickjs-${QUICKJS_VERSION}

RUN cd quickjs-${QUICKJS_VERSION} && \
    patch -p1 < no-system-modules.patch && \
    patch -p1 < how2heap.patch && \
    make qjs "-j$(nproc)" && \
    install -m755 qjs /usr/local/bin && \
    cd .. && rm -rf quickjs-${QUICKJS_VERSION}

# challenge files
RUN useradd -m -s /bin/bash ctf
COPY run.sh /home/ctf/
COPY flag.txt /home/ctf/
COPY quickjs /etc/xinetd.d/

EXPOSE 1337

CMD xinetd -dontfork