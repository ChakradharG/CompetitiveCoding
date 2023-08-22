#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, k, l, c, d, p, nl, np;
	cin >> n >> k >> l >> c >> d >> p >> nl >> np;
	int vol = k *l;
	int slices = c * d;

	int x1 = vol / nl, x2 = slices, x3 = p / np;
	int min = (x1 < x2) ? x1 : x2;
	min = (min < x3) ? min : x3;

	Log((min / n));
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
