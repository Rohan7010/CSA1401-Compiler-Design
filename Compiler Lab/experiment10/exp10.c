#include <stdio.h>

int main() {
    printf("Grammar: S->iEtS|iEtSeS|a\n");
    printf("Eliminating Left Factoring:\n");
    printf("S -> iEtS S' | a\n");
    printf("S' -> eS | epsilon\n");
    printf("E -> b\n");
    return 0;
}
