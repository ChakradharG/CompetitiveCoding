#include <iostream>
#include <bits/stdc++.h>
using namespace std;
 
void calcHeight (int height) {
    cout << (height*2) * (height*2) << endl;
}
 
void calcWidth (int width) {
    cout << (width*2) * (width*2) << endl;
}
 
 
int main() {
    int testCases;
    cin >> testCases;
    
    for(int i=0; i< testCases ; i++) {
        int height, width;
        cin >> height >> width;
        
        if (height < width) {
            if (width > (height * 2)) cout << (width * width) << endl;
            else calcHeight(height);
        }
        else {
            if (height > (width * 2)) cout << (height * height) << endl;
            else calcWidth(width);
        }
        
    }
    return 0;
}