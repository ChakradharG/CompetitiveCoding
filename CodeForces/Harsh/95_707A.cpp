// Online C++ compiler to run C++ program online
#include <iostream>
#include <map>
using namespace std;


int main() {
    int m,n;
    cin >> m >> n;
    char a;
    map<char, int> color;
    
    for(int i=0; i<m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a;
            if (color.count(a) > 0) {
                color[a] = color[a] + 1;
            }
            else {
                color[a] = 1;
            }
        }
    }
    
    if (color.count('C') + color.count('M') + color.count('Y') > 0) {
        cout << "#Color" << endl;
    }
    else {
        cout << "#Black&White" << endl;
    }
}