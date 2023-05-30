#include <stdio.h>
#include <string.h>

void demo_str() {
    char *str ="rainbow";
    printf("%s\n",str);
    printf("%8s\n",str) ; 
    printf("%.4s",str);
}

void demo_add() {
    char *str="sunday";
    int i = 1 ;
    char array[] ="Sunday" ;
    printf("%s (%p)\n",str,str) ;
    printf("%d (%p)\n",i,&i) ;
    printf("%s\n",array) ;
    for(int i=0;i<strlen(array);++i) {
        printf("str[%d]=%s (%p)\n",i,array,array);
    }
}

int main() {
    demo_add();
    return 0 ;
}