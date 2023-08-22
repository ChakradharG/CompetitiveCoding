#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int x1, x2, x3;
	cin >> x1 >> x2 >> x3;

	int min = 101, max = 0;
	if (x1 < min) { min = x1; }
	if (x1 > max) { max = x1; }
	if (x2 < min) { min = x2; }
	if (x2 > max) { max = x2; }
	if (x3 < min) { min = x3; }
	if (x3 > max) { max = x3; }

	Log((max - min));
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
