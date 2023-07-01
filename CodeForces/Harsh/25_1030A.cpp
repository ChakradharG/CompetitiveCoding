#include<iostream>
using namespace std;
 
int main() {
    int a;
    cin >> a;
    int x;
    bool isEasy = true;
    for (int i=0; i<a; i++){
        cin >> x;
        if (x == 1) {
            cout<< "HARD";
            isEasy = false;
            break;
        }
    }
    
    if (isEasy) cout<<"Easy";
    
    
    
    return 0;
}