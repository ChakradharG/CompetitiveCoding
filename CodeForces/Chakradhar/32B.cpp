#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	string s, n;
	cin >> s;

	int i = 0;
	while (i < s.length()) {
		if (s[i] == '.') {
			n += '0';
			i++;
			continue;
		} else {
			if (s[i+1] == '.') {
				n += '1';
			} else {
				n += '2';
			}
			i += 2;
			continue;
		}
	}

	Log(n);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
