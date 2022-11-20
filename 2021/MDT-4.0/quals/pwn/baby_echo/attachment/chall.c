// gcc -fpie -static-pie -o chall chall.c && strip chall
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>


int main(void) {
	unsigned int n;
	int i,c;
	char buf[32];
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	while(1) {
		printf("[1] Set Buf\n");
		printf("[2] Print Buf\n");
		printf("[3] Exit\n");
		printf("> ");
		scanf("%d", &c);
		switch(c) {
			case 1:
				printf("How much? ");
				scanf("%u", &n);
				read(0, buf, n);
				break;
			case 2:
				printf("%s\n", buf);
				break;
			default:
				goto done;
		}

	}
done:
	printf("Bye @,@ ~!");
	return 0;
}
