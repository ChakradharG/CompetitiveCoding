#include <iostream>
#include <string>
#include <cmath>
 
using namespace std;
 
int main() {
    int t;
    cin >> t;
    
    while (t-- > 0) {
        string s;
        cin >> s;
        int st = 0, lt = 0;
        
        for (int i=0; i<3;i++) {
            st += s[i] - '0';
        }
        
        for (int i=3; i<6;i++) {
            lt += s[i] - '0';
        }
        
        if (lt == st) cout << "YES" << endl;
        else cout << "NO" << endl;
        
    }
   
    
}