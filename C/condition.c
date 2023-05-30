#include <stdio.h>

void con(){
    int age ;
    printf("Please Enter Your Age=") ;
    scanf("%d",&age) ;
    if (age < 15) {
        printf("Free charge") ;
    } 
    else {
        printf("200 Baht") ;
    }
}

int main () {
    con() ;
}