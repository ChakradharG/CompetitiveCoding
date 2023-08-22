// Online C++ compiler to run C++ program online
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t-- > 0) {
       char c;
       cin >> c;
       int a = int(c) - 97;

       if (a == 2 || a == 3 || a == 4 || a == 5 || a == 14 || a == 17 || a == 18) cout << "YES" << endl;
       else cout << "NO" << endl;
        
    }
    
    return 0;
}