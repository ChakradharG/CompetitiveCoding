#include <iostream>
#include<algorithm>
using namespace std;
 
int main() {
    int t, n;
    cin >> t;
    for (int j=0; j<t; j++) {
        cin >> n;
        int arr [n];
        
        for (int i=0; i<n; i++) {
            cin >> arr[i];
        }
        
        for (int i=2; i<n; i++) {
            if (arr[i] != arr[i-1] || arr[i] != arr[i-2]) {
                if (arr[i-1] == arr[i-2]) {
                    cout << i+1 << endl;
                    break;
                }
                else if (arr[i] == arr[i-2]) {
                    cout << i << endl;
                    break;
                }
                else {
                    cout << i-1 << endl;
                    break;
                }
            }
        }   
    }
}