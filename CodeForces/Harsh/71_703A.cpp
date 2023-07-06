// Online C++ compiler to run C++ program online
#include <iostream>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t;
    int a,b;
    int m = 0,c = 0;
    while (t-- > 0) {
        cin >> a >> b;
        if (a > b) m++;
        else if (a < b) c++;
    }
    if (m > c) cout << "Mishka";
    else if (m == c) cout << "Friendship is magic!^^";
    else cout << "Chris";
    
}