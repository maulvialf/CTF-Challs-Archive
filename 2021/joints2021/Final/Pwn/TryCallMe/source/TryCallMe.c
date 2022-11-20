// gcc TryCallMe.c -o TryCallMe -no-pie -fno-stack-protector -Wl,-z,relro,-z,now

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

void TryCallMe(long int a, double b, long int c, double d, long int e, double f, long int g, double h, long int i, double j, long int k, double l){
    FILE *fptr;
    char fc;
    if((k^0xcafe1234567890) == (i^0x1234567890babe)){
        fptr = fopen((char *) &l, "r");
    }

    if(((g+c) == (a-e)) && (g != a)){
        fc = getc(fptr);
        while ((fc != EOF) && ((g^e) == 0xb333f1ac485dffe9))
        {
            if((b == 35.34) && (d == 95.68) && ((b+f) == 118.48)){
                putc(fc, stdout);
            }
            if((j == 74.53) && ((h+b) == 134.64) && ((f+d) == 178.82)){
                fc = getc(fptr);
            }
        }
    }
}

int main(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    char buf[0x64];
    read(0, buf, 0x100);
    return 1;
}