#include<iostream>
#include<string>
#include<math.h>
#include<cstdlib>
using namespace std;
 
int main() {
    int i, j, n;
    for(i=1; i<=5;i++) {
        for(j=1; j <= 5; j++) {
            cin >> n;
            if (n == 1) break;
        }
        if(n == 1) break;
    }
    
    cout << (abs(3-i) + abs(3-j));
    
    return 0;
}