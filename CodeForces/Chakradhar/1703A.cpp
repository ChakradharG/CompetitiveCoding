#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	string s, s2 = "YES";
	cin >> s;

	for (int i = 0; i < 3; i ++) {
		if (toupper(s[i]) != s2[i]) {
			Log("NO");
			return;
		}
	}
	Log("YES");
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
