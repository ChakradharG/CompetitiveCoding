#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, k, time = 240, count = 0;
	cin >> n >> k;

	time -= k;
	time /= 5;

	for (int i = 1; i <= n; i++) {
		time -= i;
		if (time >= 0) {
			count++;
		} else {
			break;
		}
	}
	Log(count);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
