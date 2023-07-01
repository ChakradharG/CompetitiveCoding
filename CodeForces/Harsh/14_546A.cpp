#include <iostream>
#include <math.h>
using namespace std;
#define Log(x) cout << x << "\n"
 
void func() {
	int a,b, w;
	cin >> a >> b >> w;
 
    
    
	int result = a*(w*(w+1)/2) - b;
 
    if(result < 0) { Log(0); }
    else Log((int)result);
}
 
int main() {
	ios::sync_with_stdio(false);
	func();
}