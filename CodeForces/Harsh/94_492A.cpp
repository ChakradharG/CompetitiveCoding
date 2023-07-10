// Online C++ compiler to run C++ program online
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    
    int n;
    cin >> n;
    int count = 1;
    int a = 1;
    int pc = 1;
    int cc = 2;
    
    while (a < n) {
        if (a + (pc + cc) > n) break;
        a = a + pc + cc;
        pc += cc;
        cc++;
        count++;
    }
    
    cout << count << endl;
    return 0;
}