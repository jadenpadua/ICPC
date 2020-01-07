#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;
// init our input number n and int array representing the height of the boxes
int n, hi[55];

int main(int argc, char *argv[]) {
    // For counting what set number we are on
    int test = 0;
    // While there are still values to cin
    while(cin>>n,n) {
        // increment our set number
        test++;
        // now sum up all numbers in our current dataset
        int sum = 0;
        for(int i = 0; i < n; i++) {
            cin >> hi[i];
            sum += hi[i];
        }
        // Calculate average number of moves by diving some by n (heigh restraint)
        sum = sum / n;
        // Sort array, two params are when height array starts until height array ends (Pointer at n)
        sort(hi, hi+n);

        // Now we go descending order calculating the moves
        int move = 0;
        for(int i = n-1; i >= 0; i--) {
            // Case where our array index is greater than sum, so our moves will increment based on the difference
            if (hi[i] > sum) move += hi[i] - sum;
                else break;
        }
        // Formatting purposes
        cout<<"Set #"<<test<<endl;
        cout<<"The minimum number of moves is "<<move<<'.'<<endl<<endl;


    }

    return 0;
}
