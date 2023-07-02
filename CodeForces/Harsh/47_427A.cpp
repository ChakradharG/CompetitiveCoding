#include <iostream>
using namespace std;
 
int main() {
    // Write C++ code here
    int m;
    cin >> m;
    int countCrime = 0;
    int countOfficer = 0;
    int val;
    
    for (int i=0 ;i<m; i++) {
        cin >> val;
        if (val == -1) {
            if (countOfficer == 0) {
                countCrime++;
            }
            else {
                countOfficer--;
            }
        }
        else {
            countOfficer += val;
        }
    }
    
    cout << countCrime;
}