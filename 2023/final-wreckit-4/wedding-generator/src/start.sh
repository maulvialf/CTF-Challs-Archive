# run sshd
/usr/sbin/sshd -D &
# run the command
su - ctf -c "cd /ctf/wedding-generator/ && ./run.sh"