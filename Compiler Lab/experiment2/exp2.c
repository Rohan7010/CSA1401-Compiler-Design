#include <stdio.h>
#include <string.h>

int main() {
    char text[100];
    printf("Enter text: ");
    gets(text);
    if(text[0] == '/' && text[1] == '/') {
        printf("Single line comment\n");
    } else if(text[0] == '/' && text[1] == '*') {
        int len = strlen(text);
        if(text[len-2] == '*' && text[len-1] == '/') {
            printf("Multi-line comment\n");
        } else {
            printf("Incomplete multi-line comment\n");
        }
    } else {
        printf("Not a comment\n");
    }
    return 0;
}
