#include <stdio.h>

int rectangle(int w,int h){
    int area ;
    area=w*h ;
    return area ;
}

void box(int w,int h){
    int i,j ;
    for(i=0;i<h;i=i+1){
        for(j=0;j<w;j=j+1){
            printf("*");
        }
    printf("\n");
    }
}

int main() {
    int w,h ;
    printf("Enter Width=");
    scanf("%d",&w) ;
    printf("Enter Height=");
    scanf("%d",&h);
    printf("Area=%d\n",rectangle(w,h)) ;
    box(w,h);
}