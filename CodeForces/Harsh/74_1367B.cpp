#include <iostream>
#include <string>
#include <cmath>
 
using namespace std;
 
int main() {
    int t;
    cin >> t;
    
    while (t-- > 0) {
        int size;
        cin  >> size;
        int a [size];
        int odd = 0, even = 0;
        for (int i=0; i<size; i++) {
            cin >> a[i];
            if (a[i] %2 == 0) even++;
            else odd++;
        }
        
        if (even != ceil(double(size)/2) || (size == 1 && odd == 1))  {
            cout << -1 << endl; 
            continue;
        }
        int count = 0;
        
        for(int i=0 ; i < size; i++) {
            if (a[i] % 2 != i % 2) count++;
        }
        
        cout << count/2 << endl;
        
    }
   
    
}