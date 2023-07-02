#include <iostream>
#include <cstring>
#include<cmath>
using namespace std;
int main()
{
    int m;
    string s;
    cin >> m;
    
    while (m--) {
        int count = 0;
        string num = "";
        cin >> s;
        
        while (s.length() > 0) {
            if (s[0] != '0') {
                int x = s[0] - '0';
                num += to_string((int)(x*pow(10,s.length()-1))) + " ";
                count++;
            }
            s = s.substr(1,s.length());
        }
         
        cout << count << endl;
        cout << num << endl;
    }
    
}