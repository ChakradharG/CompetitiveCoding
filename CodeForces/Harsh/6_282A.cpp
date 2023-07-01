#include<iostream>
#include<string>
using namespace std;
 
int main() {
    int a;
    int c=0;
    cin >> a;
    
    for(int i=0; i<a; i++) {
        
        string x;
        cin >> x;
        
        if (x.find("++") != string::npos) {
            c++;
        }
        else {
            c--;
        }
    }
    
    cout << c;
    return 0;
}