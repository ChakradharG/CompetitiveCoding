#include <iostream>
#include <vector>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, count = 0;
	cin >> n;

	vector<int> h, a;
	h.resize(n);
	a.resize(n);

	for (int i = 0; i < n; i++) {
		cin >> h[i] >> a[i];
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (i == j) continue;
			if (h[i] == a[j]) {
				count++;
			}
		}
	}

	Log(count);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
