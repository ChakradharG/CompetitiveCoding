#include <iostream>
#include <string>
#include <map>
 
using namespace std;
 
int main() {
    int num;
    map<int, int> m;
    string val;
    
    for (int i=1;i < 5; i++) {
        cin >> num;
        m.insert(pair<int, int>({i, num}));
    }
    
    cin >> val;
    int sum = 0;
    for (char c: val) {
        sum += m[c - '0'];
    }
    
    cout << sum;
    
           
   
    
}