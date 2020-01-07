#include <iostream>
using namespace std;
int main () {
    double total, input;
    for( int i = 0; i < 12; i++) {
        cin >> input;
        total += input;
    }
    cout << "$" << total / 12.0 << endl;
}
