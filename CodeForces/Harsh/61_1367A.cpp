#include <iostream>
#include<algorithm>
#include <string>
using namespace std;
 
int main() {
    int t;
    cin >> t;
    for (int j=0; j<t; j++) {
        string b;
        string a = "";
        
        cin >> b;
        a += b[0];
        
        for (int i=1; i<b.length()-1;i+=2) {
            a += b[i];
        }
        
        a += b[b.length() - 1];
        
        cout << a << endl;
        
    }
    
}