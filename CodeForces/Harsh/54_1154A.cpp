#include <iostream>
using namespace std;
 
int maxi(int a, int b) {
    return a > b ? a : b;
}
 
int main() {
    // Write C++ code here
    int x1,x2,x3,x4;
    cin >> x1 >> x2 >> x3 >> x4;
    
    int max = maxi(maxi(x1, x2), maxi(x3, x4));
    
    if (max - x1 != 0) cout << (max - x1) << " ";
    if (max - x2 != 0) cout << (max - x2) << " ";
    if (max - x3 != 0) cout << (max - x3) << " ";
    if (max - x4 != 0) cout << (max - x4) << " ";
    
}