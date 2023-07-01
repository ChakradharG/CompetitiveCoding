#include<iostream>
#include<string>
using namespace std;
 
int countStone(string s, int size) {
    int count = 0;
    
    for (int i = 1; i < size; i++) {
        if (s[i] == s[i-1]) count++;
    }
    
    return count;
    
}
 
 
int main() {
    
    string s;
    int size;
    cin >> size;
    cin >> s;
    
    cout << countStone(s, size);
    return 0;
}