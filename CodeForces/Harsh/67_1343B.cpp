#include <iostream>
#include <string>
 
using namespace std;
 
int main() {
    int t;
    cin >> t;
    while (t-- > 0) {
        int num;
        cin >> num;
        if (num == 2 || (num/2)%2 == 1) {
            cout << "NO" << endl;
            continue;
        }
        else {
            cout << "YES" << endl;
            int sum = 0;
            int j = 2;
            for (int i=0; i<num/2;i++) {
                sum += j;
                cout << j << " ";
                j += 2;
            }
            j = 1;
            for (int i =0; i<num/2-1; i++)  {
                sum -= j;
                cout << j << " ";
                j = j + 2;
            }
            
            cout << sum << endl;
            
        }
        
    }
    
}