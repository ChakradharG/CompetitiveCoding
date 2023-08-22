#include <iostream>
#include <string>
#include <cmath>
 
using namespace std;
 
long max(long a, long b) {
    return a > b ? a : b;
}
 
long min(long a, long b) {
    return a < b ? a : b;
}
 
 
int main() {
    int n;
    cin >> n;
    
    for (int i=0; i<n; i++) {
        int size;
        cin >> size;
        long mini = INFINITY, maxi = 0;
        
        long num;
        for (int j=0; j<size; j++) {
            cin >> num;
            mini = min(mini, num);
            maxi = max(maxi, num);
        }
        
        cout << int(maxi - mini) << endl;
    }
}