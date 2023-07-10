// Online C++ compiler to run C++ program online
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    
    int t;
    cin >> t;
    while (t-- > 0) {
        int a[4];
        cin >> a[0] >> a[1] >> a[2] >> a[3];
        
        int x = a[0] > a[1] ? a[0] : a[1];
        int y = a[2] > a[3] ? a[2] : a[3];
        
        sort(a, a+4);
        
        if ((x == a[2] || x == a[3]) && (y == a[2] || y == a[3])) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
        
    }
    return 0;
}