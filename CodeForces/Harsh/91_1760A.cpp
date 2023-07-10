// Online C++ compiler to run C++ program online
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    
    int t;
    cin >> t;
    while (t-- > 0) {
        int a[3];
        cin >> a[0] >> a[1] >> a[2];
        
        sort(a, a+3);
        
        cout << a[1] << endl;
    }
    return 0;
}