#include <stdio.h>
#include <stdlib.h>

/*
This is not the challenge, just a template to answer the questions.
To get the flag, answer the questions. 
There is no bug in the questionnaire.
*/

void gg(){
	system("cat flag.txt");
}

void vuln(){
	char buffer[0x20] = {0};
	fprintf(stdout, "\nEnter payload here: ");
	fgets(buffer, 0x100, stdin);
}

void main(){
	vuln();
}

