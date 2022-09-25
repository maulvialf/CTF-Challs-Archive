#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
    setbuf(stdin, NULL);

    // The flag is the name of this variable!
    int REDACTED_flagOnServer[10];
    for (int i = 0; i < 10; i++)
        REDACTED_flagOnServer[i] = i;

    printf("\nLet's see what you got...\n");
    fflush(stdout);

    int i;
    scanf("%d", &i);

    if (i <= 10) {
        printf("\nHere you go: %d!\n", REDACTED_flagOnServer[i]);
        fflush(stdout);
    }

    return 0;
}

