#include<iostream>
#include<string>
using namespace std;
int main() {
    
    string num1, num2, res="";
    cin >> num1;
    cin >> num2;
    
    for (int i=0; i<num1.length(); i++) {
        if (num1[i] != num2[i]) res += "1";
        else res += "0";
    }
    
    cout << res;
    
    
    
    
    
    return 0;
}