%%
int|float|char|void|if|else|while|return { printf("Keyword: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*                   { printf("Identifier: %s\n", yytext); }
.|\n                                     { /* ignore */ }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
