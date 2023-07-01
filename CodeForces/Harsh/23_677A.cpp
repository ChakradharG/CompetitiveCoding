#include<iostream>
#include<string>
using namespace std;
 
int main() {
    int len, height;
    int que;
    
    cin >> len >> height;
    
    int width = 0;
    
    for (int i=0; i<len; i++) {
        cin >> que;
        if (que > height) width += 2;
        else width+= 1;
    }
    
    cout << width;
    
    return 0;
    
    
}