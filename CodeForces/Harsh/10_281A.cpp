#include<iostream>
#include<string>
using namespace std;
 
string capitalize(string s) {
    
    if (!((int)s[0] >= 65 && (int)s[0] <= 91)) {
        s[0] = (char)((int)s[0] - 32);
    }
 
    return s;
    
    
}
 
 
int main() {
    
    string s;
    cin >> s;
    
    cout << capitalize(s);
    return 0;
}