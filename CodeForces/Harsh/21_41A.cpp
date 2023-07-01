#include<iostream>
#include<string>
using namespace std;
 
bool isLegal (string a, string b) {
    
    if (a.length() != b.length()) return false;
    
    for (int i=0; i<a.length(); i++) {
        if (a[i] != b[a.length() - i - 1]) return false;
        
    }
    
    return true;
}
 
 
 
int main() {
    string a,b;
    cin >> a;
    cin >> b;
    
    if (isLegal(a,b)) cout << "YES";
    else cout << "NO";
    
    return 0;
    
    
}