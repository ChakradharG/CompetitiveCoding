#include <iostream>
#include <string>
using namespace std;
 
int main() {
    long num;
    cin >> num;
    int count = 0;
    
    count += num / 100;
    num %= 100;
    count += num / 20;
    num %= 20;
    count += num / 10;
    num %= 10;
    count += num / 5;
    num %= 5;
    count += num;
    
    cout << count;
    
    
    return 0;
}