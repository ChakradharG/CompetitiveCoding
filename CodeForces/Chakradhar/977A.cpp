#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, k, mod;
	cin >> n >> k;

	while (k--) {
		mod = n % 10;
		if (mod) {
			n--;
		} else {
			n /= 10;
		}
	}

	Log(n);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
