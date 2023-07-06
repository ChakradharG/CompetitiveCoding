#include <iostream>
#include <string>
 
using namespace std;
 
int main() {
    int t;
    cin >> t;
    while (t-- > 0) {
        int n;
        cin >> n;
        int num = 0;
        int i = 0;
        while (i < n) {
            
            num++;
            if (!(num%3 == 0 || (num%10 == 3))) {
                i++;
            }
        }
        cout << num << endl;
    }
    
}