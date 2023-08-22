#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, m;
	cin >> n >> m;

	char c;
	bool bw = true;
	for (int i = 0; i < n*m; i++) {
		cin >> c;
		if (c == 'C' || c == 'M' || c == 'Y') {
			bw = false;
		}
	}

	if (bw) {
		Log("#Black&White");
	} else {
		Log("#Color");
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
