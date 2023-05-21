FROM elixir

ARG PASSWORD

RUN echo root:${PASSWORD} | chpasswd
RUN apt-get update && apt-get install -y openssh-server
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN service ssh start

WORKDIR /ctf/wedding-generator/

COPY ./lib lib
COPY mix.exs .
COPY mix.lock .
COPY start.sh .
COPY run.sh .

RUN chmod +x start.sh run.sh
RUN useradd --user-group --system --create-home --no-log-init --shell /bin/sh ctf

RUN mkdir _build deps /tmp/wedding-generator 
RUN chown ctf:ctf _build deps /tmp/wedding-generator 
RUN chmod 777 _build deps /tmp/wedding-generator
RUN touch /flag.txt

CMD ./start.sh

