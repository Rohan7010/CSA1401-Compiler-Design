#include <stdio.h>
#include <ctype.h>
int main() {
    char str[100];
    int v = 0, c = 0, i = 0;
    printf("Enter string: ");
    gets(str);
    while(str[i] != '\0') {
        char ch = tolower(str[i]);
        if(ch>='a' && ch<='z') {
            if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u') v++;
            else c++;
        }
        i++;
    }
    printf("Vowels: %d\nConsonants: %d\n", v, c);
    return 0;
}
