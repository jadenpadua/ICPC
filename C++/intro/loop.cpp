#include <iostream>
#include <cstdio>
using namespace std;


int loop(int num1,int num2) {
    char numbers[9][10] = {"one","two","three","four","five","six","seven","eight","nine"};

    for(int i = num1; i <= num2; i++) {
        if (i >= 1 && i <= 9) {
            printf("%s\n", numbers[i-1]);
            continue;
        }
        else if (i > 9 && i % 2 == 0) {
            printf("%s\n", "even");
            continue;
        }

        else if (i > 9 && i % 2 == 1) {
            printf("%s\n", "odd");
            continue;
        }
    }
    return 0;
}

int main() {
    int num1;
    int num2;
    scanf("%d %d", &num1, &num2);
    loop(num1,num2);
    return 0;
}
