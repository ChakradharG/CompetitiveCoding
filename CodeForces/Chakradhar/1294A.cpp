#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int a, b, c, n;
	cin >> a >> b >> c >> n;

	int A = n + (b + c) - (2 * a);
	if (A % 3) {
		Log("NO");
		return;
	}
	A /= 3;

	int B = A + a - b;
	int C = A + a - c;
	if (A < 0 || B < 0 || C < 0) {
		Log("NO");
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
