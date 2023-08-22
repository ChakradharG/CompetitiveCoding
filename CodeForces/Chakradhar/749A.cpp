#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n;
	cin >> n;

	Log((n / 2));

	if (n % 2) {
		for (int i = 0; i < (n/2)-1; i++) {
			cout << 2 << " ";
		}
		cout << 3 << endl;
	} else {
		for (int i = 0; i < n/2; i++) {
			cout << 2 << " ";
		}
		cout << endl;
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
