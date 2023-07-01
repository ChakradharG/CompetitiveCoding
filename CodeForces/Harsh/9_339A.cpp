#include<iostream>
#include<string>
using namespace std;
 
string newString(string a) {
    if (a.length() <= 1) {
        return a;
    }
    int count1=0, count2=0, count3 = 0;
    for (int i=0; i<a.length(); i++) {
        if (a[i] == '1') count1++;
        if (a[i] == '2') count2++;
        if (a[i] == '3') count3++;
    }
    
    string newString = "";
    for(int i=0; i<count1; i++) {
        newString += "1+";
    }
    for(int i=0; i<count2; i++) {
        newString += "2+";
    }
    for(int i=0; i<count3; i++) {
        newString += "3+";
    }
    
    return newString.substr(0, newString.size()-1);
}
 
 
int main() {
    string a;
    cin >> a;
    cout << newString(a);
    return 0;
}