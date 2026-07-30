%{
int comments = 0;
%}
%%
"//".* { comments++; }
"/*"([^*]|\*+[^*/])*\*+"/" { comments++; }
.|\n { ECHO; }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    printf("\nTotal comments: %d\n", comments);
    return 0;
}
