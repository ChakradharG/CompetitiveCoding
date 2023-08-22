#include <iostream>
#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int testCases;
    cin >> testCases;
    
    for(int i=0; i< testCases ; i++) {
        int n, q;
        cin >> n >> q;
        int a [n];
        int b [n];
        int sum = 0;
        
        for (int k = 0; k < n; k++) {
            cin >> a[k];
            sum += a[k];
        }
        
        for (int k = 0; k < n; k++) {
            cin >> b[k];
        }
        
        sort(a, a+n);
        sort(b, b+n);
        
        int p = n - 1;
        
        while (q-- > 0) {
            
            if (sum + b[p] - a[n - p - 1] > sum) {
                sum += (b[p] - a[n - p - 1]);
                p--;
            }
        }
        cout << sum << endl;
        
    }
    return 0;
}