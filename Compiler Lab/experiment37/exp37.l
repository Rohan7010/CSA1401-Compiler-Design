%{
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
