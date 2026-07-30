#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    char input[100];
    printf("Enter string: ");
    gets(input);
    int i = 0;
    while(input[i] != '\0') {
        if(isalpha(input[i])) {
            printf("Identifier: ");
            while(isalnum(input[i])) {
                printf("%c", input[i]);
                i++;
            }
            printf("\n");
        } else if(isdigit(input[i])) {
            printf("Constant: ");
            while(isdigit(input[i])) {
                printf("%c", input[i]);
                i++;
            }
            printf("\n");
        } else if(input[i] == '+' || input[i] == '-' || input[i] == '*' || input[i] == '/') {
            printf("Operator: %c\n", input[i]);
            i++;
        } else {
            i++;
        }
    }
    return 0;
}
