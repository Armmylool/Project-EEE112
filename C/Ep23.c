#include <stdio.h>

void test() {
    int height,age;
    printf("Enter your height=");
    scanf("%d", &height);
    printf("Enter your age=");
    scanf("%d", &age);
    if (height>160 && age<30) {
        printf("Congratulation You pass");
    } else {
        printf("Sorry");
    }
}

int main() {
    test();
}