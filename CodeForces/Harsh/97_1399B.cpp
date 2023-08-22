// Online C++ compiler to run C++ program online
#include <iostream>
#include <cmath>
#include <bits/stdc++.h>
using namespace std;


int main() {
    int t;
    cin >> t;
    while (t-- > 0) {
        int size;
        cin >> size;
        int a [size], b[size];
        int minA =  0x3f3f3f3f, minB = 0x3f3f3f3f;
        
        for (int i=0; i<size; i++) {
            cin >> a[i];
            minA = minA < a[i] ? minA : a[i];
        }
        
        for (int i=0; i<size; i++) {
            cin >> b[i];
            minB = minB < b[i] ? minB : b[i];
        }
        
        long long count = 0;
        
        for (int i=0; i < size; i++) {
            long long aDiff = 1ll * (a[i] - minA);
            long long bDiff = 1ll * (b[i] - minB);
            count += aDiff > bDiff ? aDiff : bDiff;
        
        }
        
        cout << count << endl;

    }
}