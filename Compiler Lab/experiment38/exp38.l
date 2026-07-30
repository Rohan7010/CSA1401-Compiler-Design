%{
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
