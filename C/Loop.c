#include <stdio.h>

void Loop() {
    int sum = 0 ;
    int i ;
    for(i=1;i<=10;i=i+2) {
        sum=sum+i ;
    }
    printf("Sum=%d",sum) ;
}

int main(){
    Loop() ;
}