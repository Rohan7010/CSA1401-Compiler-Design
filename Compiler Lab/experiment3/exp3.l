%%
[\t \n]+      /* ignore spaces, tabs, newlines */
"//".*        /* ignore single line comment */
"/*"([^*]|\*+[^*/])*\*+"/"   /* ignore multiline comment */
.             { printf("Token: %s\n", yytext); }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
