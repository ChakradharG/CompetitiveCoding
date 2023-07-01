#include <iostream>
#include <string>
using namespace std;
 
int main() {
    string s;
    int n;
    cin >> n;
    cin >> s;
    int a [26];
    int count = 26;
    
    for (int i=0; i<s.length() ;i++) {
        if (int(s[i]) >= 65 && int(s[i]) < 91) s[i] = char(int(s[i]) + 32);
        a[int(s[i]) - 97] = 1;
    }
    
    for (int i=0;i<26;i++) if (a[i] != 1) count--;
    
    if (count < 26) cout << "NO";
    else cout << "YES";
    
    
    return 0;
}
