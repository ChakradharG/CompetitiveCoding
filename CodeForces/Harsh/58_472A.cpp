
#include<iostream>
using namespace std;
 
bool checkIfComposite(int n) {
    for (int i=2; i<=n/2; i++) {
        if (n%i == 0) return true;
    }
    return false;
}
 
int main() {
    // Write C++ code here
    int n;
    cin >> n;
    int i;
    
    for (i=4; i<n; i++) {
        if (checkIfComposite(i) && checkIfComposite(n-i)) {
            cout << i << " " << (n-i);
            break;
        }
    }
    
    
    
}