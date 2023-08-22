#include <iostream>
#include <string>
#include <cmath>
#include<bits/stdc++.h>
 
using namespace std;
 
int main() {
    int t;
    cin >> t;
    
    while (t-- > 0) {
        int n;
        string s;
        set<char> tasks;
        cin >> n;
        cin >> s;
        char curr;
        bool suspicious = false;
 
        for (char c : s) {
            // cout << curr << " ";
            if (c != curr) {
                curr = c;
                if (tasks.count(c)) {
                    suspicious = true;
                    break;
                }
                else {
                    tasks.insert(c);    
                }
            }
        }
 
        if (suspicious) cout << "NO" << endl;
        else cout << "YES" << endl;
        curr = '-';
    }
   
    
}