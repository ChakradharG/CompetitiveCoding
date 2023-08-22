#include <iostream>
 
using namespace std;
 
int maxi(int arr[], int size) {
    int max = arr[0];
    for (int i=1; i<size;i++)
    {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}
 
 
int main() {
    int t;
    cin >> t;
    int arr [t];
    int sum1 = 0, sum2 = 0;
    for (int j=0; j<t; j++) {
        cin >> arr[j];    
    }
    
    int sum = 0;
    
    if (t > 1) {
        int max = maxi(arr, t);
        for (int i=0; i<t;i++) {
            sum += (max - arr[i]);
        }
    }
    
    cout << sum;
}