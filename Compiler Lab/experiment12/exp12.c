#include <stdio.h>
#include <string.h>

char input[100];
int i = 0;
void E(); void E_prime(); void T(); void T_prime(); void F();

void F() {
    if(input[i] == 'i' && input[i+1] == 'd') { i += 2; }
    else if(input[i] == '(') { i++; E(); if(input[i] == ')') i++; }
}
void T_prime() {
    if(input[i] == '*') { i++; F(); T_prime(); }
}
void T() { F(); T_prime(); }
void E_prime() {
    if(input[i] == '+') { i++; T(); E_prime(); }
}
void E() { T(); E_prime(); }

int main() {
    printf("Enter string: ");
    scanf("%s", input);
    E();
    if(i == strlen(input)) printf("Parsed Successfully\n");
    else printf("Error in parsing\n");
    return 0;
}
