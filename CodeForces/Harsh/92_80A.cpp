#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
 
int nextPrime(int a) {
    for (int i=sqrt(a); i > 1; i--) {
        if (a % i == 0) return 0;
    }    
    
    while (true) {
        a++;
        bool isPrime = true;
        for (int i=sqrt(a); i > 1; i--) {
            if (a % i == 0) {
                isPrime = false;
                break;
            }
        }
        if(isPrime) return a; 
    }
    
    
    
}
 
 
int main() {
    
    
        int m, n;
        cin >> m >> n;
        
        if (nextPrime(m) == n) {
            cout << "YES" << endl;
        }     
        else {
            cout << "NO" << endl;
        }
 
}