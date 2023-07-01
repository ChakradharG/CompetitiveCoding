#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	unsigned long a, b;
	cin >> a >> b;

	unsigned long res;
	res = a % b;

	if (res) {
		res = b - res;
	}

	Log(res);
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
