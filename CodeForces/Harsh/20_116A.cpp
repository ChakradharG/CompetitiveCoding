#include<iostream>
#include<string>
using namespace std;
 
int main() {
    int len;
    int minCount = 0;
    int currentCount = 0;
    cin >> len;
    int exit, enter;
    
    
    while(len > 0) {
        cin >> exit >> enter;
        currentCount -= exit;
        currentCount += enter;
        minCount = currentCount > minCount ? currentCount : minCount;
        len--;
    }
    
    cout << minCount;
    
    return 0;
    
    
}