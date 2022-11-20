#include <stdio.h>
#include <stdlib.h>

void init()
{
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

void greeting()
{
	printf("The Protector will print back your name\n");
}

void dontCallThisFunc()
{
	system("cat flag.txt");
}

int main()
{
	init();
	greeting();

	char firstName[0x10];
	char lastName[0x10];

	printf("First name: ");
	gets(firstName);
	printf(firstName);
	printf("\n");

	printf("Last Name: ");
	gets(lastName);
	printf(lastName);

	return 0;
}
