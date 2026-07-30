%{
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
