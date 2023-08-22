#include <iostream>
#include <cstdlib>
#include <bits/stdc++.h>
using namespace std;
 
int maxi(int a, int b) {
    return a > b ? a : b;
}
 
int main() {
    // Write C++ code here
    int t;
    cin >> t;
    
    for (int i=0; i<t; i++) {
        int n;
        cin >> n;
        int count = n;
        int a [n];
        for (int i=0; i<n; i++) {
            cin >> a[i];
        }
        if (n == 1) {
            cout << "YES" << endl;
            continue;
        }
        
        sort(a,a+n);
        
        for (int i=0; i< n; i++)
        {
            for (int j=0; j<n;j++) {
                if (i != j && a[i] !=0 && a[j] != 0 && abs(a[i] - a[j]) <= 1) {
                    if (a[i] > a[j]) a[j] = 0;
                    else a[i] = 0;
                    count--;
                }
            }
        }
        if (count == 1) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }
    
}