#include<iostream>
using namespace std;
 
int main() {
    int num, times;
    
    cin >> num >> times;
    
    while(times > 0) {
        if (num == 0) break;
        
        
        if (num % 10 == 0) num = num/10;
        else num--;
        times--;
    }
    
    cout << num;
    
    
    
    return 0;
}