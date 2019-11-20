#include <iostream>
using namespace std;

void isEvenWeight(int w) {
    if (w > 2 && w % 2 == 0) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }
}

int main() {
    int w;
    cin >> w;
    isEvenWeight(w);

    return 0;
}
