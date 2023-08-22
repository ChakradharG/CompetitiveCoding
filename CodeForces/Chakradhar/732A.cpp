#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int k, r;
	cin >> k >> r;

	int x = k % 10;
	for (int i = 1; i <= 9; i++) {
		if (((x * i) % 10) == r) {
			Log(i);
			return;
		}
	}
	for (int i = 1; i <= 9; i++) {
		if (((x * i) % 10) == 0) {
			Log(i);
			return;
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
