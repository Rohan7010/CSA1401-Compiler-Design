#include <stdio.h>

int main() {
    printf("Grammar: S->(L)|a, L->L,S|S\n");
    printf("Eliminating Left Recursion:\n");
    printf("S -> (L) | a\n");
    printf("L -> S L'\n");
    printf("L' -> , S L' | epsilon\n");
    return 0;
}
