#include <stdio.h>
#include <string.h>

struct SymbolTable {
    char name[20];
    char type[20];
} st[10];

int main() {
    strcpy(st[0].name, "x"); strcpy(st[0].type, "int");
    strcpy(st[1].name, "y"); strcpy(st[1].type, "float");
    printf("Symbol Table:\n");
    for(int i=0; i<2; i++) {
        printf("%s : %s\n", st[i].name, st[i].type);
    }
    return 0;
}
