%{
int chars = 0, lines = 0, words = 0;
%}
%%
[a-zA-Z]+ { words++; chars += yyleng; }
\n        { lines++; chars++; }
.         { chars++; }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    printf("Lines: %d\nWords: %d\nChars: %d\n", lines, words, chars);
    return 0;
}
