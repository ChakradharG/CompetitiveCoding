// Online C++ compiler to run C++ program online
#include <iostream>
#include <cmath>
#include <bits/stdc++.h>
using namespace std;


int maxi (int a, int b) {
    return a > b ? a : b;
}

int main() {
    int t;
    cin >> t;
    while (t-- > 0) {
        int a,b,c, n;
        cin >> a >> b >> c >> n;
        
        int max = maxi(maxi(a,b), maxi(b,c));
        
        n -= ((max - a) + (max - b) + (max - c));
        
        if (n >= 0 && n%3 == 0) cout << "YES" << endl;
        else cout << "NO" << endl;
        
    }
}