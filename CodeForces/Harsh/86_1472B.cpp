// Online C++ compiler to run C++ program online
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t-- > 0) {
        
        int n;
        cin >> n;
        int c1 = 0, c2 = 0;
        int num;
        
        while (n-- > 0) {
            cin >> num;
            if (num == 1) c1++;
            else c2++;
        }
        
        if (c1%2 == 0 && c2%2 == 0) cout << "YES" << endl;
        else if (c2 % 2 != 0 && c1 % 2 == 0 && c1 > 0) cout << "YES" << endl;
        else cout << "NO" << endl;
        
    }
    
    return 0;
}