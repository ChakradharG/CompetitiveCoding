#include <iostream>
#include <cstdlib>
using namespace std;
 
int main() {
    // Write C++ code here
    int x1, x2, x3;
    cin >> x1 >> x2 >> x3;
    
    int meetX1 = abs(x1-x2) + abs(x1-x3);
    int meetX2 = abs(x1-x2) + abs(x2-x3);
    int meetX3 = abs(x3-x2) + abs(x1-x3);
    
    if (meetX1 < meetX2 && meetX1 < meetX3) cout << meetX1;
    else if (meetX2 < meetX1 && meetX2 < meetX3) cout << meetX2;
    else cout << meetX3;
}