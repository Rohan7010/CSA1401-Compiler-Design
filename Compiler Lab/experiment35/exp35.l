%%
^[0-9]+$ { printf("It is a digit\n"); }
.*       { printf("Not a digit\n"); }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
