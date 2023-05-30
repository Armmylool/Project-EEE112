#include <stdio.h>

void seq() {
    double celcius,farenheit ;
    printf("Enter Celcius=") ;
    scanf("%lf",&celcius) ;
    farenheit=(1.8*celcius)+32 ;
    printf("Celcius %lf = Farenheit %lf",celcius,farenheit) ;
}
int main() {
    seq() ;
    return 0 ;
}