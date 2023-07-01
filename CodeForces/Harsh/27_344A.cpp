#include<iostream>
#include<string>
using namespace std;
 
int main() {
    int n;
    cin >> n;
    int groups = 1;
    string currentPolarity="", lastPolarity = "";
    
    cin >> lastPolarity;
    
    for(int i=1; i<n; i++) {
        cin >> currentPolarity;
        if (currentPolarity[0] == lastPolarity[1]) groups++;
        lastPolarity = currentPolarity;
    }
    
    cout << groups;
    
    return 0;
}