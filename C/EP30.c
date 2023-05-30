#include <stdio.h>

int main() {
    int a ;
    int P ;
    for (int i=9;i<=11;++i) {
        for (a=1;a<=12;++a) {
            P=i*a ;
            printf("%d * %d = %d\n",i,a,P) ;
        }
        printf("\v") ;
    }
}