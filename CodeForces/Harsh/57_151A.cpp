// Online C++ compiler to run C++ program online
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int min (int a, int b) {
    return a < b ? a : b;
}


int main() {
    // Write C++ code here
    int n, k, l, c, d, p, nl, np;
    
    cin >> n >> k >> l >> c >> d >> p >> nl >> np;
    
    int totalToast = k*l / nl ;
    int totalSalt = p / np;
    int totalSlices = c*d;
    
    cout << min(totalToast, min(totalSalt, totalSlices)) / n;
}
