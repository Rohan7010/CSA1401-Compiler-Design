%{
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
