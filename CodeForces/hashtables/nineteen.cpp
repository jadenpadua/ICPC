#include <bits/stdc++.h>
using namespace std;

int main() {
    map<char,int> count;
    string s; cin>>s;
    for (auto c: s) ++count[c];
    cout << min({(count['n']-1)/2,count['i'],count['e']/3, count['t']});
    return 0;
}
