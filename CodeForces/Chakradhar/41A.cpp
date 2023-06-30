#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	string s, t;
	cin >> s >> t;

	int n = s.length();
	if (n != t.length()) {
		Log("NO");
		return;
	}
	bool flag = true;

	for (int i = 0; i < n; i++) {
		if (s[i] != t[n-i-1]) {
			flag = false;
			break;
		}
	}

	if (flag) {
		Log("YES");
	} else {
		Log("NO");
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
