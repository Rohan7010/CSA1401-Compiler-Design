%%
"http://"[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})+ { printf("Valid URL\n"); }
"https://"[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})+ { printf("Valid URL\n"); }
.* { printf("Invalid URL\n"); }
%%
int yywrap() { return 1; }
int main() {
    yylex();
    return 0;
}
