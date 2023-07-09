#include <iostream>
#include <string>
using namespace std;
 
int main() {
    
    int t;
    cin >> t;
    while (t-- > 0) {
        string s;
        cin >> s;
        
        if (s.length() %2 == 1) cout << "NO" << endl;
        else {
            int i=0, j=s.length()/2;
            bool isSquare = true;
            while (j < s.length()) {
                if (s[i++] != s[j++]) {isSquare = false; break;}
            }
            if (isSquare) cout << "YES" << endl;
            else cout << "NO" << endl;
        }
    }
    return 0;
}