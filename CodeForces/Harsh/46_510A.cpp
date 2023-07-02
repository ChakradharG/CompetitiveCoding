#include <iostream>
using namespace std;
 
int main() {
    // Write C++ code here
    int m,n;
    cin >> m >> n;
    bool printFirst = false;
    
    for (int i=0; i<m; i++) {
        for (int j = 0; j<n; j++) {
            if (i%2 == 0) {
                cout << "#";
            }
            else {
                if (j == (n-1) && i%4 == 1) {
                    cout << "#";
                }
                else if (j == 0 && i%4 == 3) {
                    cout << "#";
                }
                else {
                    cout << ".";    
                }
            }
        }
        cout << endl;
    }
    
    
    return 0;
}