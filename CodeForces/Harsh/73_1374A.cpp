// Online C++ compiler to run C++ program online
#include <iostream>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t-- > 0) {
        int x,y,n;
        cin >> x >> y >> n;
        
        int num = (n - (n % x));
        
        if (n%x == y) cout << n << endl;
        else if ((n - num) == y) cout << num << endl;
        else if ((n - num) < y) cout << num - (x - y) << endl;
        else cout << num + y << endl;
    }
   
    
}