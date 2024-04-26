#include <stdio.h>
#include <stdlib.h>

int main(int ac, char** av) {
    if (ac != 2) {
        printf("Usage: %s <shellcode>\n", av[0]);
        return 1;
    }
    char *shellcode = av[1];
    printf("Executing shellcode...\n");
    (*(void(*)())shellcode)();
    return 0;
}
// gcc [-m32] -z execstack test.c -o test && ./test <shellcode>
