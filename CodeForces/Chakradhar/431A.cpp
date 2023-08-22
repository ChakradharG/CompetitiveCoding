#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	array<int, 5> a;
	cin >> a[1] >> a[2] >> a[3] >> a[4];

	string s;
	cin >> s;

	long long cal = 0;
	for (char c: s) {
		cal += a[c - 48];
	}

	Log(cal);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
