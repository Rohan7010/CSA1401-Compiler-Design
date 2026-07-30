%{
int wc = 0, lc = 0;
%}
%%
[ \t]   { wc++; }
[\n]    { lc++; }
.       { /* ignore */ }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    printf("Whitespaces: %d\nNewlines: %d\n", wc, lc);
    return 0;
}
