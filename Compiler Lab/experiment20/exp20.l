%%
[0-9]+(\.[0-9]+)? { printf("Constant: %s\n", yytext); }
.|\n              { /* ignore */ }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
