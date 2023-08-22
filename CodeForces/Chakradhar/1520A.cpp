#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n;
	cin >> n;

	string s;
	cin >> s;
	array<int, 26> arr{};

	char prev = s[0];
	for (char c: s) {
		if ((c != prev) && (arr[c - 65] != 0)) {
			Log("NO");
			return;
		} else {
			arr[c - 65] = 1;
			prev = c;
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
