#include <iostream>
#include <math.h>
using namespace std;
#define Log(x) cout << x << "\n"
 
void func() {
	int a;
	cin >> a ;
 
    int count = 0;
    
   
    count += a / 5;
    a = a%5;
 
    count += a / 4;
    a = a%4;
 
    count += a / 3;
    a = a%3;
 
    count += a / 2;
    a = a%2;
 
    count += a / 1;
    a = a%1;
 
 
    Log(count);
 
}
 
int main() {
	ios::sync_with_stdio(false);
	func();
}