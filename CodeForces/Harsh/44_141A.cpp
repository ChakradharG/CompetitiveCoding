#include <iostream>
#include <string>
using namespace std;
 
int main() {
    // Write C++ code here
    string host, residence, pile;
    cin >> host;
    cin >> residence;
    cin >> pile;
    
    if (pile.length() != (host.length() + residence.length())) {
        cout << "NO";
        return 0;
    }
    
    int arr [26] = {0};
    
    for (char i: host) {
        arr[int(i) - 65] += 1;
    }
    
    for (char i: residence) {
        arr[int(i) - 65] += 1;
    }
    
    for (char i: pile) {
        arr[int(i) - 65] = arr[int(i) - 65] - 1;
    }
    
    for (int i=0; i<26; i++) {
        if (arr[i] != 0) {
            cout << "NO";
            return 0;
        }
    }
    
    cout << "YES";
    
 
    return 0;
}