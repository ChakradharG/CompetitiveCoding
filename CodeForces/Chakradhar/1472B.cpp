#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, x, c1 = 0, c2 = 0;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> x;
		if (x == 1) c1++;
		else c2++;
	}

	if (c1 % 2) {
		Log("NO");
	} else if (c1 == 0) {
		if (c2 % 2) {
			Log("NO");
		} else {
			Log("YES");
		}
	} else {
		Log("YES");
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
