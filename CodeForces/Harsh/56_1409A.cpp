#include <iostream>
#include <cstdlib>
using namespace std;
 
 
int main() {
    // Write C++ code here
    int t;
    cin >> t;
    
    for (int i=0; i<t; i++) {
        long a,b;
        cin >> a >> b;
        
        int count = (abs(a - b)/10);
        
        count += (abs(a-b)%10) == 0? 0: 1;
        
        cout << count << endl;
    }
}