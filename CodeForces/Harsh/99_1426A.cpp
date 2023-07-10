// Online C++ compiler to run C++ program online
#include <iostream>
#include <cmath>
#include <bits/stdc++.h>
using namespace std;


int main() {
    int t;
    cin >> t;
    while (t-- > 0) {
        int n, x;
        cin >> n >> x;
        if (n < 3) {
            cout << 1 << endl;
            continue;
        }
        
        int count = 1;
        int temp = 0;
        while (true) {
            count++;
            if (n >= ((temp * x) + 3) && n <= (((temp+1) * x) + 2)) {
                break;
            }
            temp++;
        }
        
        cout << count << endl;
        

    }
}