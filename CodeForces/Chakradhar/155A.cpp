#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	unsigned int n, min, max, x, count = 0;
	cin >> n;
	cin >> x;
	min = x;
	max = x;

	while (n--) {
		cin >> x;
		if (x < min) {
			min = x;
			count++;
		}
		if (x > max) {
			max = x;
			count++;
		}
	}

	Log(count);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
