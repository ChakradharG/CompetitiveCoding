// Online C++ compiler to run C++ program online
#include <iostream>
#include <map>
using namespace std;


int main() {
    int t;
    cin >> t;
    while (t-- > 0) {
        int h,m;
        cin >> h >> m;
        
        int hr = 23 - h;
        int mr = 60 - m;
        
        cout << (hr*60) + mr << endl;
        
        
        
        
    }
}