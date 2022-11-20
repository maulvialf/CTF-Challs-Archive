#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>

#define N_BOOK 16

typedef struct Book {
	uint32_t num_page;
	char title[24];
	char *desc;
} Book;

Book* books[N_BOOK];

void read_strline(char* buf, unsigned int size) {
	int n = read(0, buf, size);
	if(n < 0) {
		fprintf(stderr, "read error\n");
		exit(1);
	}
	buf[n-1] = '\0';
}

unsigned long int read_int() {
	char buf[24];
	memset(buf, 0, sizeof(buf));
	read_strline(buf, 23);
	return strtoul(buf, NULL, 10);
}

uint16_t get_idx_book(void) {
	uint16_t idx;
	printf("idx book: ");
	idx = read_int();
	if(idx >= N_BOOK) {
		fprintf(stderr, "Invalid book index\n");
		exit(1);
	}
	return idx;
}

int menu() {
	printf("*** Books v1.0 ***\n");
	printf("[1] Create book\n");
	printf("[2] Edit book\n");
	printf("[3] Print book\n");
	printf("[4] Delete book\n");
	printf("[5] Exit\n");
	printf("> ");
	return (int)read_int();
}

int main(void) {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	int choice = 0;
	char buf[40] = {0};
	uint16_t idx = 0;
	size_t desc_len;
	while(1) {
		choice = menu();
		switch(choice) {
			case 1:
				idx = get_idx_book();
				if(books[idx]) {
					printf("Book already exists\n");
					break;
				}

				books[idx] = malloc(sizeof(Book));
				printf("title: ");
				read_strline(books[idx]->title, 24);
				printf("num page: ");
				books[idx]->num_page = read_int();
				printf("desc len: ");
				desc_len = read_int();
				char* desc = malloc(desc_len);
				if(!desc) {
					fprintf(stderr, "malloc error\n");
					break;
				}
				printf("desc: ");
				read_strline(desc, desc_len);
				books[idx]->desc = desc;
				break;
			case 2:
				idx = get_idx_book();
				if(!books[idx]) {
					printf("Book not exists\n");
					break;
				}
				Book* book = books[idx];

				printf("title: ");
				read_strline(book->title, 24);

				printf("num page: ");
				book->num_page = read_int();

				printf("desc len: ");
				desc_len = read_int();
				free(book->desc);
				desc = malloc(desc_len);

				printf("desc: ");
				read_strline(desc, desc_len);
				book->desc = desc;
				break;
			case 3:
				idx = get_idx_book();
				if(!books[idx]) {
					printf("Book not exists\n");
					break;
				}
				printf("num page : %d\n", books[idx]->num_page);
				printf("title : %s\n", books[idx]->title);
				printf("description : %s\n", books[idx]->desc);
				break;
			case 4:
				idx = get_idx_book();
				if(!books[idx]) {
					printf("Book not exists\n");
					break;
				}
				free(books[idx]->desc);
				free(books[idx]);
				books[idx] = NULL;
				break;
			case 5:
				goto done;
				break;
			default:
				printf("Not implemented\n");
				break;
		}
		printf("Done\n");
	}
done:
	printf("Bye!\n");
}
