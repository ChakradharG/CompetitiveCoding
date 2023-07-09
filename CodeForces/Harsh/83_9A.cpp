#include <iostream>
using namespace std;
 
int maxi(int a, int b) {
    return a > b ? a : b;
}
 
 
int main() {
    int a,b;
    
    cin >> a >> b;
    int val = 6 - maxi(a,b) + 1;
    
    if (val == 0) cout << "0/1" << endl;
    else if (val == 6) cout << "1/1" << endl;
    else if (val % 2 == 0) cout << val/2 << "/" << "3";
    else if (val % 3 == 0) cout << val/3 << "/" << "2";
    else cout << val << "/" << 6;
    
    return 0;
}