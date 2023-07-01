#include <iostream>
#include <math.h>
using namespace std;
#define Log(x) cout << x << "\n"
 
void func() {
	double a, b, result;
	cin >> a >> b;
 
	double numerator = log(b/a);
	double denominator = log(3.0/2.0);
 
	result = numerator / denominator;
	if (ceil(result) == result) {
		result++;
	} else {
		result = ceil(result);
	}
 
	Log((int)result);
}
 
int main() {
	ios::sync_with_stdio(false);
	func();
}