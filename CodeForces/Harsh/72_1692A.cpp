#include <iostream>
#include <string>
 
using namespace std;
 
int main() {
    int t;
    cin >> t;
    
    while (t-- > 0) {
        int a,j;
        int count = 0;
        cin >> a;
        for (int i=0; i<3; i++) {
            cin >> j;
            if (j > a) count++;
        }
        
        cout << count << endl;
    }
   
    
}