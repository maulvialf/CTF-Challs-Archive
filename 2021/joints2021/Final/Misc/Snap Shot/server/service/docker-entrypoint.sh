#!/bin/sh

if [ ! -f "/etc/ssh/ssh_host_rsa_key" ]; then
	# generate fresh rsa key
	ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa
fi

iptables -A INPUT -m state --state NEW,ESTABLISHED,RELATED --source wrapper -p tcp --dport 2222 -j ACCEPT;
iptables -A INPUT -m state --state NEW,ESTABLISHED,RELATED --source localhost -p tcp --dport 2222 -j ACCEPT;
iptables -A INPUT -m state --state NEW,ESTABLISHED,RELATED -p tcp --dport 2222 -j DROP;

if [ ! -f "/etc/ssh/ssh_host_dsa_key" ]; then
	# generate fresh dsa key
	ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa
fi

#prepare run dir
if [ ! -d "/var/run/sshd" ]; then
  mkdir -p /var/run/sshd
fi

exec "$@"


