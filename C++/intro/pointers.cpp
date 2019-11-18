#include <stdio.h>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
void update(int *a,int *b) {
    int temp = *a;
    (*a) = (*a) + (*b);
    (*b) = abs((temp) - (*b));
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    cin >> a >> b;

    update(pa, pb);
    cout << a << "\n" << b;

    return 0;
}

