#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **av){
    if (ac != 2){
        printf("Usage: %s <env_var>\n", av[0]);
        return 1;
    }
    printf("%p\n", getenv(av[1]));
    return 0;
}
