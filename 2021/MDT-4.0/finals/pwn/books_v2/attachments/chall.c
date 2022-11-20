#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>

#define N_AUTHOR 16
#define N_BOOK 512

typedef struct Author {
	uint16_t refcnt;
	char name[40];
} Author;

typedef struct Book {
	uint32_t num_page;
	char title[24];
	char *desc;
	Author* author;
} Book;

Author* authors[N_AUTHOR];
Book* books[N_BOOK];

void* Malloc(size_t n) {
	void* res = malloc(n);
	if(!res) {
		fprintf(stderr, "Malloc error\n");
		exit(1);
	}
	return res;
}

void read_strline(char* buf, unsigned int size) {
	int n = read(0, buf, size);
	if(n < 0) {
		fprintf(stderr, "read error\n");
		exit(1);
	}
	buf[n-1] = '\0';
}

unsigned long int read_int() {
	char buf[21];
	memset(buf, 0, sizeof(buf));
	read_strline(buf, 20);
	return strtoul(buf, NULL, 10);
}

Book* new_book(uint32_t num_page, char* title, char* description, Author* author) {
	Book* book = Malloc(sizeof(Book));
	book->num_page = num_page;
	strncpy(book->title, title, 24);
	book->desc = description;
	book->author = author;
	return book;
}

Author* new_author(char* name) {
	Author* author = Malloc(sizeof(Author));
	author->refcnt = 1;
	memset(author->name, 0, 40);
	strncpy(author->name, name, 40);
	return author;
}

Author* get_author(uint16_t idx) {
	if(idx >= N_AUTHOR) {
		fprintf(stderr, "Invalid author index\n");
		return NULL;
	}
	if(!authors[idx]) {
		fprintf(stderr, "Author not exist\n");
		return NULL;
	}
	authors[idx]->refcnt++;
	return authors[idx];
}

void put_author(Author* author) {
	if(--author->refcnt == 0) {
		free(author);
	}
}

uint16_t get_idx_author(void) {
	uint16_t idx;
	printf("idx author: ");
	idx = read_int();
	if(idx >= N_AUTHOR) {
		fprintf(stderr, "Invalid author index\n");
		exit(1);
	}
	return idx;
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
	printf("*** Books v2.0 ***\n");
	printf("[1] Create author\n");
	printf("[2] Edit author\n");
	printf("[3] Delete author\n");
	printf("[4] Create book\n");
	printf("[5] Edit book\n");
	printf("[6] Print book\n");
	printf("[7] Delete book\n");
	printf("[8] Exit\n");
	printf("> ");
	return (int)read_int();
}

void print_list_author(void) {
	for(int i = 0; i < N_AUTHOR; i++) {
		if(authors[i]) {
			printf("[%d] %s\n", i, authors[i]->name);
		}
	}
}

int main(void) {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	int choice = 0;
	char buf[40] = {0};
	uint16_t idx = 0;
	uint16_t l = 0;
	while(1) {
		choice = menu();
		switch(choice) {
			case 1:
				idx = get_idx_author();
				if(authors[idx]) {
					printf("Author already exists\n");
					break;
				}
				printf("author name length: ");
				l = read_int();
				if(l > 40) {
					fprintf(stderr, "Too big\n");
					break;
				}
				printf("author name: ");
				read_strline(buf, l);
				authors[idx] = new_author(buf);
				break;
			case 2:
				idx = get_idx_author();
				if(!authors[idx]) {
					printf("Author not exists\n");
					break;
				}
				printf("author name length: ");
				l = read_int();
				if(l > 40) {
					fprintf(stderr, "Too big\n");
					break;
				}
				printf("new author name: ");
				read_strline(authors[idx]->name, l);
				break;
			case 3:
				idx = get_idx_author();
				if(!authors[idx]) {
					printf("Author not exists\n");
					break;
				}
				put_author(authors[idx]);
				authors[idx] = NULL;
				break;
			case 4:
				idx = get_idx_book();
				if(books[idx]) {
					printf("Book already exists\n");
					break;
				}

				print_list_author();
				printf("choose author\n");

				Author* author = get_author(get_idx_author());
				if(!author) {
					break;
				}

				printf("title: ");
				read_strline(buf, 24);
				printf("num page: ");
				uint32_t num_page = read_int();
				printf("desc len: ");
				uint32_t desc_len = read_int();
				if(desc_len > 0x800) {
					desc_len = 0x800;
				}
				char* desc = Malloc(desc_len);
				printf("desc: ");
				read_strline(desc, desc_len);

				books[idx] = new_book(num_page, buf, desc, author);
				break;
			case 5:
				idx = get_idx_book();
				if(!books[idx]) {
					printf("Book not exists\n");
					break;
				}
				Book* book = books[idx];
				printf("num page: ");
				book->num_page = read_int();
				printf("title: ");
				read_strline(book->title, 24);

				printf("desc len: ");
				desc_len = read_int();
				if(desc_len > 0x800) {
					desc_len = 0x800;
				}
				free(book->desc);
				desc = Malloc(desc_len);
				printf("desc: ");
				read_strline(desc, desc_len);
				book->desc = desc;
				break;
			case 6:
				idx = get_idx_book();
				if(!books[idx]) {
					printf("Book not exists\n");
					break;
				}
				printf("num page : %d\n", books[idx]->num_page);
				printf("title : %s\n", books[idx]->title);
				printf("description : %s\n", books[idx]->desc);
				printf("author: %s\n", books[idx]->author->name);
				break;
			case 7:
				idx = get_idx_book();
				if(!books[idx]) {
					printf("Book not exists\n");
					break;
				}
				put_author(books[idx]->author);
				free(books[idx]->desc);
				free(books[idx]);
				books[idx] = NULL;
				break;
			case 8:
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
