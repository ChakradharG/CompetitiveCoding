#include <iostream>
#include <string>
using namespace std;
 
int main() {
    string s;
    getline(cin, s);
    int a [26];
    int count = 0;
    
    for (int i=0; i<s.length() ;i++) {
        if (int(s[i]) >= 97 && int(s[i]) < 123) {
            a[int(s[i]) - 97] = 1;
        }
    }
    
    for (int i=0;i<26;i++) 
    {
        if (a[i] == 1) 
        {
            count++;
        }
    }
    
    cout << count;
    
    return 0;
}