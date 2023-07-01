#include<iostream>
#include<string>
using namespace std;
int main() {
    
    string hate = "I hate ";
    string love = "I love ";
    string final = "I hate ";
    
    int n;
    cin >> n;
    
    for (int i=1; i<n;i++) {
        if (i%2 == 1) final += "that " + love;
        else final += "that " + hate;
    }
    
    cout << final << "it";
    
    
    
    
    return 0;
}