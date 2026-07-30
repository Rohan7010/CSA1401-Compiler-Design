%%
"old_word" { printf("new_word"); }
.|\n       { ECHO; }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
