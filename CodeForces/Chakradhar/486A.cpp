#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	unsigned long long n, div, mod;
	cin >> n;

	div = n / 2;
	mod = n % 2;

	if (mod) {
		cout << "-";
		div++;
	}
	Log(div);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
