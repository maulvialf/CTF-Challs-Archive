// gcc ./chal.c -o chal -no-pie -fno-stack-protector
#include<signal.h>
#include<stdio.h>
#include<string.h>
#include<unistd.h>

void kill_on_timeout(int sig) {
  if (sig == SIGALRM) {
    _exit(0);
  }
}


void nobaper() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	signal(SIGALRM, kill_on_timeout);
	alarm(60);
}

int main() {
  nobaper();

  char str2[40];
  char str1_length[32];
  str1_length[0] = '\x32';
  char str2_length[32];
  str2_length[0] = '\x32';
  char str1[32];

  write(1, "A simple program to compare string\n", 35);
  write(1, "String 1: ", 10);
  fgets(str1, (unsigned char) str1_length[0], stdin);
  write(1, "String 2: ", 10);
  fgets(str2, (unsigned char) str2_length[0], stdin);

  if(!strncmp(str1, str2, 32)) {
  	write(1, "String match\n", 13);
  } else {
  	write(1, "String doesn't match\n", 21);
  }

  return 0;
}
