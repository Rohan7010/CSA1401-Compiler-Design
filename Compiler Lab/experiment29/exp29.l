%%
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
