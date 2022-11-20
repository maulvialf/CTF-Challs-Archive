// docker run --rm -v $PWD:/pwd --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -d --name chal -i ubuntu:20.04
// docker exec -it chal bash
// apt update && apt install -y make gcc
#include<stdio.h>
#include<string.h>
#include<stdbool.h>

int LENGTH = 24;

bool check_length(char *password) {
    return(strlen(password) == LENGTH);
}

bool is_all_char_in_charset(char *password) {
    for(int i = 0; i < strlen(password); i++) {
        if(password[i] >= 'a' && password[i] <= 'z') continue;
        else if(password[i] >= '0' && password[i] <= '9') continue;
        else if(password[i] == '_') continue;
        return false;
    }
    return true;
}

unsigned int process(char *substr) {
    unsigned int res = (int)substr[0] ^ (int)substr[1];
    res *= (int)substr[2];
    res += (int)substr[3];
    res ^= ((int)substr[0] * (int)substr[0] * (int)substr[0]);
    res *= (int)substr[0];
    res -= (int)substr[2];
    res %= 0xffffff;
    return res;
}

int main() {
    char password[LENGTH+1];
    char *check = "82174ed8dbebcee3bdd38bd65e44f5c6490d";
    char result[36] = "";
    char *pos;

    fputs("Flag: ", stdout);
    fgets(password, LENGTH+1, stdin);
    if ((pos=strchr(password, '\n')) != NULL)
        *pos = '\0';

    if(check_length(password) && is_all_char_in_charset(password)) {
        for(int i=0; i<LENGTH/4; i++) {
            char to_be_processed[5];
            char tmp_result[7];
            memcpy(to_be_processed, &password[i*4], 4);
            to_be_processed[4] = '\0';
            sprintf(tmp_result, "%x", process(to_be_processed));
            tmp_result[6] = '\0';
            strcat(result, tmp_result);
        }

        if(!strcmp(result, "82174ed8dbebcee3bdd38bd65e44f5c6490d")) {
            printf("\nMAYBE this is the flag: JOINTS21{%s}\n", password);
            return 0;
        }
    }
    puts("Boooo");
    return 1;
}