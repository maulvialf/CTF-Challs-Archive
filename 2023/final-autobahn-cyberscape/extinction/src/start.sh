# run sshd
/usr/sbin/sshd -D &
# run the command
deno run --allow-net --allow-read --allow-write --allow-env main.ts