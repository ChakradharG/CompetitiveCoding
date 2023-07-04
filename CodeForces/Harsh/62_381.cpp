#include <iostream>
#include<algorithm>
#include <string>
using namespace std;
 
int main() {
    int t;
    cin >> t;
    int a [t];
    int sum1 = 0, sum2 = 0;
    for (int j=0; j<t; j++) {
        cin >> a[j];    
    }
    int count = 0;
    int i = 0, j = t-1;
    while (i <= j) {
        
        if (count %2 == 0) {
            if (a[i] >= a[j]) {
                sum1 += a[i];
                i++;
            }
            else {
                sum1 += a[j];
                j--;
            }
        }
        else {
            if (a[i] >= a[j]) {
                sum2 += a[i];
                i++;
            }
            else {
                sum2 += a[j];
                j--;
            }
        }
        count++;
    }
    
    cout << sum1 << " " << sum2;
    
}