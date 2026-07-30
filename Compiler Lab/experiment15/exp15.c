#include <stdio.h>
int main() {
    FILE *fp = fopen("input.txt", "r");
    if(!fp) return 1;
    char ch;
    int chars=0, words=0, lines=0;
    while((ch = fgetc(fp)) != EOF) {
        chars++;
        if(ch == ' ' || ch == '\t') words++;
        if(ch == '\n') { lines++; words++; }
    }
    printf("Chars: %d, Words: %d, Lines: %d\n", chars, words, lines);
    fclose(fp);
    return 0;
}
