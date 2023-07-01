#include<iostream>
#include<string>
#include<set>
using namespace std;
int main() {
    unsigned long s1,s2,s3,s4;
    cin >> s1 >> s2 >> s3 >> s4;
    
    set<unsigned long> c;
    
    c.insert(s1);
    c.insert(s2);
    c.insert(s3);
    c.insert(s4);
    
    cout << (4 - c.size());
    
    
}