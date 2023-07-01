#include<iostream>
#include<string>
using namespace std;
 
string arrangeQueue (string a, int len) {
    
    for (int i=0; i<len-1; i++) {
        if (a[i] == 'B' && a[i+1] == 'G') {
            a[i] = 'G';
            a[i+1] = 'B';
            i += 1;
        }
    }
 
    return a;
}
 
 
 
int main() {
    int len, time;
    string que;
    
    cin >> len >> time;
    cin >> que;
    
    for (int i=0; i<time; i++) {
        que = arrangeQueue(que, len);
    }
    
    cout << que;
    
    return 0;
    
    
}