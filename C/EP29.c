#include <stdio.h>

int main () {
    double a ;
    // printf("Enter your ounces :") ;
    // scan("%d",&a) ;
    for (int i =1;i<=10;i++) {
        a = 28.3495 * i ;
        printf("%d ounces = %lf grams\n",i,a) ;
        }
}
