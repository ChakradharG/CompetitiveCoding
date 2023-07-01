// Online C++ compiler to run C++ program online
#include <iostream>
#include <string>
using namespace std;
 
 
int main() {
    // Write C++ code here
    int n;
    cin >> n;
    int a,b;
    int mod;
    
    for (int i=0; i<n; i++) 
    {
        cin>>a>>b;
        if (a < b) {
            cout << b - a << endl;
        }
        else {
            mod = a % b;    
            if (mod == 0) cout << 0 << endl;
            else {
                cout << (b - mod) << endl;
            }
            
        }
    }
 
    return 0;
}