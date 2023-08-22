#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	array<int, 4> a;

	cin >> a[0] >> a[1] >> a[2] >> a[3];
	int mi = 0;
	for (int i = 1; i < 4; i++) {
		if (a[i] > a[mi]) {
			mi = i;
		}
	}

	int j = 0;
	for (int i = 0; i < 4; i++) {
		if (i != mi) {
			cout << a[mi] - a[i] << " ";
		}
	}
	cout << endl;
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
