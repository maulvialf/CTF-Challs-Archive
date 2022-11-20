#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void sice() {
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
  system("date +'%s'");
}

void vuln() {
  char buf[0x20];
  fgets(buf, 0x1000, stdin);
  close(0);
  close(1);
  close(2);
}

int main(int argc, char const *argv[]) {
  sice();
  vuln();
  return 0;
}
