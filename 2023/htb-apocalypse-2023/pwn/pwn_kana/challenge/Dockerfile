# FROM ubuntu:22.04
FROM ubuntu@sha256:34fea4f31bf187bc915536831fd0afc9d214755bf700b5cdb1336c82516d154e

# Setup environ
ENV user kana
ENV prob_port 13334

# Install packages
RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirror.kakao.com/g" /etc/apt/sources.list \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y socat \
 && rm -rf /var/lib/apt/lists/*

# Change permission
RUN chmod 1733 /tmp /var/tmp /dev/shm

# Additional configuration
RUN adduser --disabled-password --gecos "" $user
ADD ./kana /home/$user/kana
ADD ./flag /home/$user/flag

RUN chown -R root:$user /home/$user/
RUN chown root:$user /home/$user/kana
RUN chown root:$user /home/$user/flag

RUN chmod 2755 /home/$user/kana
RUN chmod 440 /home/$user/flag

# final
WORKDIR /home/$user
CMD socat -T 15 TCP-LISTEN:$prob_port,reuseaddr,fork EXEC:/home/$user/kana,su=$user
EXPOSE $prob_port
