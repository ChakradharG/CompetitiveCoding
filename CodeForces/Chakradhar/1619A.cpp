#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	string s;
	cin >> s;
	int n = s.length();

	if (n % 2 != 0) {
		Log("NO");
		return;
	}

	string s1 = s.substr(0, n / 2);
	string s2 = s.substr(n / 2, n);

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
