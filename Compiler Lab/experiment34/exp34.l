%%
^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/[0-9]{4}$ { printf("Valid DOB\n"); }
.* { printf("Invalid DOB\n"); }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
