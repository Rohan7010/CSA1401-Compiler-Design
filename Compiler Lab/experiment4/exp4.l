%%
"+"|"-"|"*"|"/" { printf("Arithmetic Operator: %s\n", yytext); }
.|\n            { /* ignore */ }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
