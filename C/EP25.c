#include <stdio.h>

int main() {
    int age ;
    int Ticket ;
    printf("Enter your age=");
    scanf("%d",&age);
    Ticket= age < 5 || age > 60 ? 0 : 50 ;
    printf("Ticket=%d",Ticket) ;
}