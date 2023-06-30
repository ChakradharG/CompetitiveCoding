#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, p, q, count = 0;
	cin >> n;

	while (n--) {
		cin >> p >> q;

		if ((q - p) > 1) {
			count++;
		}
	}

	Log(count);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
