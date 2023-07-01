#include<iostream>
#include<string>
using namespace std;
 
int main() {
    string num;
    cin >> num;
    
    int luckyCount = 0;
    
    for (char i: num) {
        if (i == '4' || i == '7') luckyCount++;
       
    }
    
    if (luckyCount == 4 || luckyCount == 7) cout << "YES";
    else cout << "NO";
    
    return 0;
}