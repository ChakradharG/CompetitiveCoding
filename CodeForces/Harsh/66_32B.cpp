#include <iostream>
#include <string>
 
using namespace std;
 
int main() {
    string code;
    cin >> code;
    int i = 0;
    while (i < code.length()) {
        if (code[i] == '.') cout << 0;
        else if (code[i] == '-' && code[i+1] == '.') {
            cout << 1;
            i++;
        }
        else {
            cout << 2;
            i++;
        }
        i++;
    }
    
} 