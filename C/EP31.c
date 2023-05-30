#include <stdio.h>

int main() {
    int sum =0 ;
    int s ;
    printf("Enter your number:") ;
    scanf("%d",&s);
    while(s!=0){
        sum=sum+s ;
        printf("Enter your number:") ;
        scanf("%d",&s);
    }
    printf("Sum =%d",sum);
}