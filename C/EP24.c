#include <stdio.h>

// int main() {
//     char d ;
//     printf("[m]ocha\n");
//     printf("[l]atte\n");
//     printf("[t]ea\n");
//     printf("Insert your menu:");
//     scanf("%c",&d);
//     if(d=='m'){
//         printf("40");
//     }else if(d =='l') {
//         printf("50");
//     }else if(d=='t') {
//         printf("60");
//     }else {
//         printf("Invalid");
//     }
// }

void test() {
    int age;
    int ticket ;
    printf("Enter your age:");
    scanf("%d",&age);
    if (age<7 || age>60) {
        printf("Ticket = 0");
    } else {
        printf("Ticket = 50");
    }  
    // printf("Ticket =%d",ticket) ;
}

int main() {
    test();
}