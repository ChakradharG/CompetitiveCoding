#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	string s;
	cin >> s;

	int i = 0, n = s.length() / 2, s1 = 0, s2 = 0;
	for (char c: s) {
		if (i < n) {
			s1 += c + 48;
		} else {
			s2 += c + 48;
		}
		i++;
	}

	if (s1 == s2) {
		Log("YES");
	} else {
		Log("NO");
	}
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
