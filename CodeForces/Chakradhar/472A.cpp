#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n;
	cin >> n;
	if (n % 2) {
		cout << 9 << " " << n - 9 << endl;
	} else {
		cout << 8 << " " << n - 8 << endl;
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
