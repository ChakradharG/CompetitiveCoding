#include<iostream>
#include<string>
using namespace std;
 
int checkSize(string a, string b) {
    for(int i=0; i<a.length(); i++) {
        if ((int) tolower(a[i]) > (int) tolower(b[i])) {
            return 1;
        }
        else if ((int) tolower(a[i]) < (int) tolower(b[i])) {
            return -1;
        }
    }
    
    return 0;
}
 
int main() {
    string a,b;
    cin >> a;
    cin >> b;
    cout << checkSize(a,b);
    return 0;
}