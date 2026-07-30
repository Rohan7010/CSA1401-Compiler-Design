%%
[0-9]+"+"[0-9]+ { printf("Addition\n"); }
[0-9]+"-"[0-9]+ { printf("Subtraction\n"); }
[0-9]+"*"[0-9]+ { printf("Multiplication\n"); }
[0-9]+"/"[0-9]+ { printf("Division\n"); }
.|\n { /* ignore */ }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
