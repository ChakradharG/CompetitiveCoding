#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
 
int main() {
    int t;
    cin >> t;
    
    while (t-- > 0) {
       int size;
       cin >> size;
       int a [size];
       
       for (int i=0; i<size; i++) cin >> a[i];
       
       sort(a, a+size);
       int min = INFINITY;
       int i=1;
       while(i < size) {
           min = min < (a[i] - a[i-1]) ? min : (a[i] - a[i-1]);
           i++;
       }
       
       cout << min << endl;
    }
    
    return 0;
}