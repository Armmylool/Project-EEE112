#include <stdio.h>

void demo_Loop() 
{
    int i ;
    for(i=1;i<10;i++)
    {
        printf("%d\n",i) ;
    }
    printf("End & มีทั้งหมด=%d",--i) ;
}

int main()
{
    demo_Loop();
}