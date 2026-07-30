#include <stdio.h>
int main() {
    printf("Expression: x = a + b * c\n");
    printf("Three address code:\n");
    printf("t1 = b * c\n");
    printf("t2 = a + t1\n");
    printf("x = t2\n");
    return 0;
}
