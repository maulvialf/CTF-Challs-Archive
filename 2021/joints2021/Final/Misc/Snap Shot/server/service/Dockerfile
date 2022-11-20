FROM alpine

RUN apk --update --no-cache add sudo imagemagick x11vnc openssh xvfb openrc
RUN apk --update --no-cache add iptables netcat-openbsd
RUN rm -rf /tmp/* /var/cache/apk/* /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_dsa_key

RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/g;s/#Port 22/Port 2222/g;s/#PubkeyAuthentication yes/PubkeyAuthentication yes/g' /etc/ssh/sshd_config
RUN echo -e 'joints21ulala\njoints21ulala' | adduser user
RUN echo -e 'jHqnjetJMZMNCvWLtgLxmbRwhm8tzJFzN\njHqnjetJMZMNCvWLtgLxmbRwhm8tzJFzN' | adduser joints

RUN echo "user ALL=(joints) NOPASSWD: /usr/bin/display" >> /etc/sudoers
RUN echo "joints ALL=(root) NOPASSWD: /root/get_flag" >> /etc/sudoers

RUN sudo -u joints sh -c 'mkdir -p ~/.ssh'
RUN sudo -u joints sh -c 'wget -O ~/.ssh/id_rsa https://cutt.ly/ovklGuR'
RUN sudo -u joints sh -c 'wget -O - https://cutt.ly/MvkzoNr >> ~/.ssh/authorized_keys'
RUN sudo -u joints sh -c 'chmod 400 -R ~/.ssh/*'
RUN sudo -u joints sh -c 'echo -e "ls -la\nwget -O ~/.ssh/id_rsa https://cutt.ly/ovklGuR\nwget -O - https://cutt.ly/MvkzoNr >> ~/.ssh/authorized_keys\nchmod 400 -R ~/.ssh/*" > ~/.ash_history'
RUN chmod 600 /home/joints/.ash_history

COPY docker-entrypoint.sh /usr/local/bin
COPY src/get_flag /root

RUN chown -R root:root /root
RUN chmod 700 -R /root
RUN rc-update add sshd

EXPOSE 2222

ENTRYPOINT ["sh", "/usr/local/bin/docker-entrypoint.sh"]
CMD ["/usr/sbin/sshd","-D"]
