#include <iostream>
#include<algorithm>
using namespace std;
 
int main() {
    int n,k;
    cin >> n >> k;
    int count = 0;
    int arr [n];
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }
    
    // Using sorting here so that once the sum goes above 5
	//  we can break the loop from there. Can be done in O(n) if sorting is not used
	// then just iterate over all the elements one by one.
	sort(arr, arr + n);
    
    for (int i=0; i<n; i++) {
        if (arr[i] + k <= 5) {
            count++;
        }
		else {
			break;
		}
    }
    



    cout << (count)/3;
    
}