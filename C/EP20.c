#include <stdio.h>

int demo_integer() {
    int m=50 ;
    int n=20 ;
    printf("m=%d\nn=%d",m,n) ;
}

int demo_float() {
    float r=3.1412 ;
    printf("Radius=%.2f\n",r) ;
    printf("%5f",r) ;
}

void demo_char() {
    char i='Z' ;
    printf("%d %c %x %#X",i,i,i,i) ;
}

int main() {
    demo_char();
    return 0 ;
}