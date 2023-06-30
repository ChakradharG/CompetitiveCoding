#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, a, b;
	cin >> n;

	int curr = 0, max = 0;

	while (n--) {
		cin >> a >> b;
		curr = curr - a + b;
		if (curr > max) {
			max = curr;
		}
	}

	Log(max);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
