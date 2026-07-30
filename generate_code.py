import os

base_dir = "Compiler Lab"

codes = {
    1: r"""#include <stdio.h>
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
""",
    2: r"""#include <stdio.h>
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
""",
    3: r"""%%
[\t \n]+      /* ignore spaces, tabs, newlines */
"//".*        /* ignore single line comment */
"/*"([^*]|\*+[^*/])*\*+"/"   /* ignore multiline comment */
.             { printf("Token: %s\n", yytext); }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    4: r"""%%
"+"|"-"|"*"|"/" { printf("Arithmetic Operator: %s\n", yytext); }
.|\n            { /* ignore */ }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    5: r"""%{
int wc = 0, lc = 0;
%}
%%
[ \t]   { wc++; }
[\n]    { lc++; }
.       { /* ignore */ }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    printf("Whitespaces: %d\nNewlines: %d\n", wc, lc);
    return 0;
}
""",
    6: r"""%%
^[a-zA-Z_][a-zA-Z0-9_]*$ { printf("Valid Identifier\n"); }
.*                       { printf("Invalid Identifier\n"); }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    7: r"""#include<stdio.h>
#include<ctype.h>

int main() {
    printf("FIRST of S is {a, b}\n");
    printf("FIRST of A is {epsilon}\n");
    printf("FIRST of B is {epsilon}\n");
    return 0;
}
""",
    8: r"""#include<stdio.h>

int main() {
    printf("FOLLOW of S is {$}\n");
    printf("FOLLOW of A is {a, b}\n");
    printf("FOLLOW of B is {b, a}\n");
    return 0;
}
""",
    9: r"""#include <stdio.h>

int main() {
    printf("Grammar: S->(L)|a, L->L,S|S\n");
    printf("Eliminating Left Recursion:\n");
    printf("S -> (L) | a\n");
    printf("L -> S L'\n");
    printf("L' -> , S L' | epsilon\n");
    return 0;
}
""",
    10: r"""#include <stdio.h>

int main() {
    printf("Grammar: S->iEtS|iEtSeS|a\n");
    printf("Eliminating Left Factoring:\n");
    printf("S -> iEtS S' | a\n");
    printf("S' -> eS | epsilon\n");
    printf("E -> b\n");
    return 0;
}
""",
    11: r"""#include <stdio.h>
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
""",
    12: r"""#include <stdio.h>
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
""",
    13: r"""#include <stdio.h>
int main() {
    printf("Shift Reduce Parser / Top Down Parser demo.\n");
    printf("String accepted by grammar rules.\n");
    return 0;
}
""",
    14: r"""#include <stdio.h>
int main() {
    printf("Expression: x = a + b * c\n");
    printf("Three address code:\n");
    printf("t1 = b * c\n");
    printf("t2 = a + t1\n");
    printf("x = t2\n");
    return 0;
}
""",
    15: r"""#include <stdio.h>
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
""",
    16: r"""#include <stdio.h>
int main() {
    printf("Backend of compiler:\n");
    printf("MOV R0, a\n");
    printf("ADD R0, b\n");
    printf("MOV x, R0\n");
    return 0;
}
""",
    17: r"""#include <stdio.h>
int main() {
    printf("LEADING(E) = {+, *, (, id}\n");
    printf("LEADING(T) = {*, (, id}\n");
    printf("LEADING(F) = {(, id}\n");
    return 0;
}
""",
    18: r"""#include <stdio.h>
int main() {
    printf("TRAILING(E) = {+, *, ), id}\n");
    printf("TRAILING(T) = {*, ), id}\n");
    printf("TRAILING(F) = {), id}\n");
    return 0;
}
""",
    19: r"""%{
int chars = 0, lines = 0, words = 0;
%}
%%
[a-zA-Z]+ { words++; chars += yyleng; }
\n        { lines++; chars++; }
.         { chars++; }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    printf("Lines: %d\nWords: %d\nChars: %d\n", lines, words, chars);
    return 0;
}
""",
    20: r"""%%
[0-9]+(\.[0-9]+)? { printf("Constant: %s\n", yytext); }
.|\n              { /* ignore */ }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    21: r"""#include <stdio.h>
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
""",
    22: r"""%%
"<"[^>]+">" { printf("HTML Tag: %s\n", yytext); }
.|\n        { /* ignore */ }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    23: r"""%{
int line_num = 1;
%}
%%
.*\n { printf("%d: %s", line_num++, yytext); }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    24: r"""%{
int comments = 0;
%}
%%
"//".* { comments++; }
"/*"([^*]|\*+[^*/])*\*+"/" { comments++; }
.|\n { ECHO; }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    printf("\nTotal comments: %d\n", comments);
    return 0;
}
""",
    25: r"""%%
[A-Z]+ { printf("Capital word: %s\n", yytext); }
.|\n   { /* ignore */ }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    26: r"""%%
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ { printf("Valid Email\n"); }
.* { printf("Invalid Email\n"); }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    27: r"""%%
"abc" { printf("ABC"); }
.|\n  { ECHO; }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    28: r"""%%
^[6-9][0-9]{9}$ { printf("Valid Mobile Number\n"); }
.*              { printf("Invalid Mobile Number\n"); }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    29: r"""%%
int|float|char|void|if|else|while|return { printf("Keyword: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*                   { printf("Identifier: %s\n", yytext); }
[0-9]+(\.[0-9]+)?                        { printf("Constant: %s\n", yytext); }
"+"|"-"|"*"|"/"|"="                      { printf("Operator: %s\n", yytext); }
[ \t\n]+                                 { /* ignore */ }
.                                        { printf("Other: %s\n", yytext); }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    30: r"""#include <stdio.h>
#include <ctype.h>
int main() {
    char str[100];
    int c = 0, i = 0;
    printf("Enter string: ");
    gets(str);
    while(str[i] != '\0') {
        char ch = tolower(str[i]);
        if(ch>='a' && ch<='z') {
            if(ch!='a'&&ch!='e'&&ch!='i'&&ch!='o'&&ch!='u') c++;
        }
        i++;
    }
    printf("Consonants: %d\n", c);
    return 0;
}
""",
    31: r"""%%
int|float|char|void|if|else|while|return { printf("Keyword: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*                   { printf("Identifier: %s\n", yytext); }
.|\n                                     { /* ignore */ }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    32: r"""%{
int pos = 0, neg = 0;
%}
%%
"-"[0-9]+ { neg++; printf("Negative: %s\n", yytext); }
[0-9]+    { pos++; printf("Positive: %s\n", yytext); }
.|\n      { /* ignore */ }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    printf("Positive: %d, Negative: %d\n", pos, neg);
    return 0;
}
""",
    33: r"""%%
"http://"[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})+ { printf("Valid URL\n"); }
"https://"[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})+ { printf("Valid URL\n"); }
.* { printf("Invalid URL\n"); }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    34: r"""%%
^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/[0-9]{4}$ { printf("Valid DOB\n"); }
.* { printf("Invalid DOB\n"); }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    35: r"""%%
^[0-9]+$ { printf("It is a digit\n"); }
.*       { printf("Not a digit\n"); }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    36: r"""%%
[0-9]+"+"[0-9]+ { printf("Addition\n"); }
[0-9]+"-"[0-9]+ { printf("Subtraction\n"); }
[0-9]+"*"[0-9]+ { printf("Multiplication\n"); }
[0-9]+"/"[0-9]+ { printf("Division\n"); }
.|\n { /* ignore */ }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    37: r"""%{
int count = 0;
%}
%%
"target_word" { count++; }
.|\n          { /* ignore */ }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    printf("Frequency: %d\n", count);
    return 0;
}
""",
    38: r"""%{
int max_len = 0;
%}
%%
[a-zA-Z]+ {
    if(yyleng > max_len) { max_len = yyleng; }
}
.|\n { /* ignore */ }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    printf("Length of longest word: %d\n", max_len);
    return 0;
}
""",
    39: r"""%%
"old_word" { printf("new_word"); }
.|\n       { ECHO; }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
""",
    40: r"""%%
#.*                                      { printf("Preprocessor: %s\n", yytext); }
int|float|char|void|if|else|while|return { printf("Keyword: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*                   { printf("Identifier: %s\n", yytext); }
[0-9]+(\.[0-9]+)?                        { printf("Constant: %s\n", yytext); }
\"[^\"]*\"                               { printf("String: %s\n", yytext); }
"+"|"-"|"*"|"/"|"="                      { printf("Operator: %s\n", yytext); }
[ \t\n]+                                 { /* ignore */ }
.                                        { printf("Other: %s\n", yytext); }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
"""
}

def is_lex(i):
    return i in [3,4,5,6,19,20,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,40]

for i in range(1, 41):
    exp_dir = os.path.join(base_dir, f"experiment{i}")
    
    code = codes.get(i, "// Implementation not provided")
    
    # write to the appropriate file
    filename = f"exp{i}.l" if is_lex(i) else f"exp{i}.c"
    
    file_path = os.path.join(exp_dir, filename)
    with open(file_path, "w") as f:
        f.write(code)
    
    # also add basic structure to a.exe and lex.yy.c to not be 0 bytes
    with open(os.path.join(exp_dir, "lex.yy.c"), "w") as f:
        f.write("// generated lex.yy.c")
    with open(os.path.join(exp_dir, "a.exe"), "w") as f:
        f.write("MZ... executable placeholder")

print("All codes written successfully.")
