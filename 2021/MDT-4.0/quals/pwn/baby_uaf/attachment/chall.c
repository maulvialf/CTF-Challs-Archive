#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
unsigned long int read_int();
void readline(char* buf, unsigned int size);
typedef struct {
	unsigned int size;
	char* buf;
} ss;
ss* arr[8];

int menu() {
	printf("[1] Alloc\n");
	printf("[2] Edit\n");
	printf("[3] Print\n");
	printf("[4] Delete\n");
	printf("[5] Exit\n");
	printf("> ");
	return (int)read_int();
}

void readline(char* buf, unsigned int size) {
	int n = read(0, buf, size);
	if(n < 0) {
		fprintf(stderr, "read error\n");
		exit(1);
	}
	if(n == 0) return;
	buf[n-1] = '\0';
}

unsigned long int read_int() {
	char buf[21];
	memset(buf, 0, sizeof(buf));
	readline(buf, 20);
	return strtoul(buf, NULL, 10);
}

static unsigned int get_idx() {
	unsigned int idx = (unsigned int)read_int();
	if(idx >= 8) {
		fprintf(stderr, "Index too large\n");
		exit(1);
	}
	return idx;
}

int main(void) {
	int c, idx;
	unsigned int size;
	char* buf;
	ss* tmp;
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	while(1) {
		c = menu();
		switch(c) {
			case 1:
				printf("idx: ");
				idx = get_idx();
				if(arr[idx] != NULL ) {
					printf("Already allocated\n");
					break;
				}
				if(!(tmp = malloc(sizeof(ss)))) {
					fprintf(stderr, "malloc error\n");
					exit(1);
				}
				printf("set size: ");
				size = read_int();
				if(size < 0x410 || size > 0x800) {
					fprintf(stderr, "Too large or Too small\n");
					exit(1);
				}
				if(!(buf = malloc(size))) {
					fprintf(stderr, "malloc error\n");
					exit(1);
				}
				printf("set content: ");
				readline(buf, size);
				tmp->buf = buf;
				tmp->size = size;
				arr[idx] = tmp;
				printf("done\n");
				break;
			case 2:
				printf("idx: ");
				idx = get_idx();
				if(arr[idx] == NULL) {
					printf("not allocated\n");
					break;
				}
				printf("set content: ");
				readline(arr[idx]->buf, arr[idx]->size);
				break;
			case 3:
				printf("idx: ");
				idx = get_idx();
				if(arr[idx] == NULL) {
					printf("not allocated\n");
					break;
				}
				printf("content: %s\n", arr[idx]->buf);
				break;
			case 4:
				printf("idx: ");
				idx = get_idx();
				if(arr[idx] == NULL) {
					printf("not allocated\n");
					break;
				}
				free(arr[idx]->buf);
				break;
			case 5:
				printf("Bye Q·Q ~!\n");
				goto done;
		}
	}
done:
	return 0;
}
