// Online C++ compiler to run C++ program online
#include <iostream>
#include <math.h>
using namespace std;

int main() {
    // Write C++ code here
    int n;
    long double candies;
    
    cin >> n;
    for (int i=0; i<n; i++) {\
        cin >> candies;
        cout << fixed << long(ceil(double(candies)/2) - 1) << endl;
    }
    
    return 0;
}