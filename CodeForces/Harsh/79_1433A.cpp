#include <iostream>
 
using namespace std;
 
int main() {
    int n;
    cin >> n;
    
    for (int i=0; i<n; i++) {
        int num;
        cin >> num;
        
        int currentDigit = num%10;
        int cdl = 0;
        
        while (num > 0) {
            num /= 10;
            cdl++;
        }
        
        cout << (10 * (currentDigit - 1)) + (cdl*(cdl+1)/2) << endl;   
        
    }
}