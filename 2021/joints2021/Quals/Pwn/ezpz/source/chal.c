// docker run --rm -v $PWD:/pwd --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -d --name chal -i ubuntu:20.04
// docker exec -it chal bash
// apt update && apt install -y make gcc socat
// socat TCP-LISTEN:5000,reuseaddr,fork EXEC:./exec.sh,su=nobody
#include<stdio.h>
#include<stdlib.h>
#include<signal.h>
#include<unistd.h>

void win() {
    system("cat flag.txt");
}

void kill_on_timeout(int sig) {
    if (sig == SIGALRM) {
        _exit(0);
    }
}



void nobaper() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    signal(SIGALRM, kill_on_timeout);
    alarm(60);
}

void vuln() {
    char in[32];
    read(0, in, 41);
}

int main() {
    nobaper();
    printf("Here's a little gift: %9$p\n");
    vuln();
    
    return 0;
}