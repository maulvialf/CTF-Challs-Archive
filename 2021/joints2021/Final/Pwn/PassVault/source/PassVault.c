// gcc PassVault.c -fstack-protector-all -pie -masm=intel -o PassVault

#include<stdlib.h>
#include<unistd.h>
#include<stdio.h>
#include<string.h>
#include<signal.h>

typedef struct credential{
    char username[16];
    char password[16];
    char note[32];
} cred;

cred credentials[10];

int isDebugOn = 0;

void toggle_debug_mode();

void sigsegv_handler(){
    long int v_rbp, v_rsp;
    __asm__(
        ".intel_syntax noprefix;"
        "mov %0, [rbp+0xb0];"
        "mov %1, [rbp+0xd8];"
        :"=&r" (v_rsp), "=&r" (v_rbp)
        );
    printf("SIGSEGV at RSP %p RBP %p\n", v_rsp, v_rbp);
    toggle_debug_mode();
    exit(-1);
}

void sigill_handler(){
    long int v_rip;
    __asm__(
        ".intel_syntax noprefix;"
        "mov %0, [rbp+0xb8];"
        :"=&r" (v_rip)
        );
    printf("SIGILL at address %p\n", v_rip);
    toggle_debug_mode();
    exit(-1);
}

void toggle_debug_mode(){
    if(isDebugOn){
        puts("DEBUG MODE : OFF");
        isDebugOn = 0;
        signal(SIGSEGV, SIG_DFL);
        signal(SIGILL, SIG_DFL);
    }
    else{
        puts("DEBUG MODE : ON");
        isDebugOn = 1;
        signal(SIGSEGV, sigsegv_handler);
        signal(SIGILL, sigill_handler);
    }
}

void read_str(char *buf, int c){
    int ctr = read(0, buf, c);
    if(buf[ctr-1] == '\n'){
        buf[ctr-1] = 0;
    }
}

void add_creds(){
    int i;
    for(i=0; i<10; i++){
        if(credentials[i].username[0] == 0){
            break;
        }
    }
    if(i > 9){
        puts("FULL");
    }
    else{
        printf("Username : ");
        read_str(credentials[i].username, 16);
        printf("Password : ");
        read_str(credentials[i].password, 16);
        printf("Note : ");
        read_str(credentials[i].note, 32);
    }
}

void edit_creds(){
    int c;
    printf("Index : ");
    scanf("%d", &c);
    getchar();

    if((c < 10) && (credentials[c].username[0] != 0)){
        printf("New username : ");
        read_str(credentials[c].username, 16);
        printf("New password : ");
        read_str(credentials[c].password, 16);
        printf("Note : ");
        read_str(credentials[c].note, 32);
    }
    else{
        puts("Invalid index!");
    }
}

void delete_creds(){
    int c;
    printf("Index : ");
    scanf("%d", &c);
    getchar();

    if((c < 10) && ((long int*) credentials[c].username != NULL)){
        memset(credentials[c].username, '\x00', sizeof(cred));
    }
    else{
        puts("Invalid index!");
    }
}

void show_creds(){
    puts("TO DO");
}

void print_menu(){
    puts("\nMenu");
    puts("1. Add");
    puts("2. Edit");
    puts("3. Show");
    puts("4. Delete");
    puts("5. Exit");
    printf("> ");
}

void init(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
}

int main(){
    int choice;
    init();
    while (1){
        print_menu();
        scanf("%d", &choice);
        getchar();
        switch (choice)
        {
        case 1:
            add_creds();
            break;
        
        case 2:
            edit_creds();
            break;

        case 3:
            show_creds();
            break;

        case 4:
            delete_creds();
            break;

        case 5:
            exit(1);
            break;

        case 0:
            toggle_debug_mode();
            break;
        
        default:
            puts("Invalid choice!");
            break;
        }
    }
    return 1;
}