#include <iostream>
#include <math.h>
#include<string>
using namespace std;
#define Log(x) cout << x << "\n"
 
string correct(string s) {
    
    int small =0, big = 0;
    string smallString, bigString;
    
    
    
    for(char i :  s) {
        if ((int)i >= 65 && (int)i <= 91) big++;
        else small++;
        smallString += tolower(i);
        bigString += toupper(i);
    }
    
    return small >= big ? smallString: bigString;
    
    
    
    
}
 
 
 
void func() {
    string s;
    cin >> s;
    
    
 
    
 
 
    Log(correct(s));
 
}
 
int main() {
	ios::sync_with_stdio(false);
	func();
}