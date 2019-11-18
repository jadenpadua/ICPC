#include <bits/stdc++.h>

using namespace std;


int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Write Your Code Here
    char numbers[10][6] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    if ( n > 9) {
        printf("Greater than 9");
    }
    else {
        printf("%s",numbers[n-1]);
    }
    return 0;
}
