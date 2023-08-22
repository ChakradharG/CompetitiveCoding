#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n;
	cin >> n;

	int height = 0, level = 0, sum = 0;
	while (sum < n) {
		height++;
		level += height;
		sum += level;
	}
	if (sum > n) height--;

	Log(height);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
