#include <stdio.h>

void demo1() 
{
    char d ;
    printf("[m]ocha\n");
    printf("[T]ea\n");
    printf("Enter your menu:") ;
    scanf("%c",&d) ;
    switch(d) {
        case 'm' :
        printf("50") ;
        break ;
        case 'T' :
        printf("30") ;
        break ;
        default : 
        printf("Please select a valid menu") ;
    }
}
int main() {
    demo1();
}