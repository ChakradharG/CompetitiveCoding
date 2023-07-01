// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
 
 
 
int main() {
    int n;
    cin >> n;
    int a [n];
    int count = 0;
    int max = 0, min = 101;
    int maxIndex = 0, minIndex = 0;
    
    
    for (int i=0; i<n;i++) {
        cin >> a[i];
        if (a[i] > max) { 
            max = a[i];
            maxIndex = i;
        }
        
        if (a[i] <= min) { 
            min = a[i];
            minIndex = i;
        }
        
    }
    
    count = maxIndex + (n - (minIndex + 1));
    
    if (maxIndex > minIndex) count--;
    
    cout << count;
    return 0;
}