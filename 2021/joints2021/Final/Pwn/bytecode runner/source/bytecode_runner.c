// gcc bytecode_runner.c -o bytecode_runner -pie -fstack-protector-all -Wl,-z,relro,-z,now

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>

typedef struct bytecode
{
    unsigned char name[0x18];
    unsigned char size;
    unsigned char code[];
} bcode;

bcode *byteData[20];
char *name;

void read_str(char *buf, unsigned char c){
    unsigned char ctr;
    ctr = read(0, buf, c);
    buf[--ctr] = 0;
}

void read_hex_str(char *buf, unsigned char c){
    unsigned char i,j;
    unsigned char t,tt[2];

    for(i=0; i<c; i++){
        j = 0;
        while (j<2){
            t = getchar();
            if((t >= 0x30 && t <= 0x39) || (t >= 0x41 && t <= 0x46) || (t >= 0x61 && t <= 0x66)){
                tt[j++] = t;
            }
        }
        buf[i] = (char) strtol(tt, NULL, 16);
    }
}

unsigned int read_int(){
    char a[8];
    read_str(a, 8);
    return atoi(a);
}

void add(int isStrInput){
    unsigned int inx;
    unsigned char tmp_size;
    printf("Index : ");
    inx = read_int();
    if((inx < 20) && byteData[inx] == NULL){
        printf("Code size : ");
        tmp_size = read_int();
        byteData[inx] = malloc(0x19 + tmp_size);
        byteData[inx]->size = tmp_size;
        
        printf("Name : ");
        read_str(byteData[inx]->name, 0x18);

        if(isStrInput){
            printf("String bytecode : ");
            read_str(byteData[inx]->code, tmp_size);
        }
        else{
            printf("Hex string bytecode : ");
            read_hex_str(byteData[inx]->code, tmp_size);
        }
    }
    else{
        puts("Invalid index!");
    }
}

void view(){
    unsigned int inx;
    printf("Index : ");
    inx = read_int();
    if((inx < 20) && byteData[inx] != NULL){
        puts("");
        puts(byteData[inx]->name);
        for(int i=0; i<byteData[inx]->size; i++){
            if((i%16 == 0) && (i != 0)){
                puts("");
            }
            printf("%02x ", byteData[inx]->code[i]);
        }
        puts("");
    }
    else{
        puts("Invalid index!");
    }
}

void delete(){
    unsigned int inx;
    printf("Index : ");
    inx = read_int();
    if((inx < 20) && byteData[inx] != NULL){
        free(byteData[inx]);
        printf("%s deleted!\n", byteData[inx]->name);
        byteData[inx] = NULL;
    }
    else{
        puts("Invalid index!");
    }
}

void login(){
    name = malloc(0x160);
    printf("\nUsername : ");
    read_str(name, 0xff);
}

void run(){
    puts("Sorry, in development :(");
}

void print_menu(){
    puts("\nMenu");
    puts("1. Add string bytecode");
    puts("2. Add hex string bytecode");
    puts("3. View bytecode");
    puts("4. Run bytecode");
    puts("5. Delete bytecode");
    puts("6. Logout");
    puts("7. Exit");
    printf("[%s]> ", name);
}

void init(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
}

int main(){
    init();
    unsigned int choice=0;
    while (1)
    {
        login();
        while (choice != 6)
        {
            print_menu();
            choice = read_int();
            switch (choice)
            {
            case 1:
                add(1);
                break;
            case 2:
                add(0);
                break;
            case 3:
                view();
                break;
            case 4:
                run();
                break;
            case 5:
                delete();
                break;
            case 6:
                break;
            case 7:
                exit(1);
                break;
            
            default:
                puts("Invalid choice!");
                break;
            }
        }
        choice = 0;
    }
    
    return 0;
}