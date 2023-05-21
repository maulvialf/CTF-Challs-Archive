FROM denoland/deno:latest
ARG PASSWORD

RUN echo root:${PASSWORD} | chpasswd
RUN apt-get update && apt-get install -y openssh-server
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN service ssh start

WORKDIR /ctf/ctf-archiver/
COPY . .

RUN chmod +x start.sh
CMD ./start.sh


