#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, x, s = 0, d = 0;
	cin >> n;

	vector<int> a;
	for (int i = 0; i < n; i++) {
		cin >> x;
		a.push_back(x);
	}

	int left = 0, right = n-1;
	while (true) {
		if (left > right) break;
		if (a[right] > a[left]) {
			s += a[right];
			right--;
		} else {
			s += a[left];
			left++;
		}

		if (left > right) break;
		if (a[right] > a[left]) {
			d += a[right];
			right--;
		} else {
			d += a[left];
			left++;
		}
	}
	cout << s << " " << d << endl;
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
