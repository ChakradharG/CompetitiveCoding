#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, m = 0, c = 0, mi, ci;
	cin >> n;

	while (n--) {
		cin >> mi >> ci;
		if (mi > ci) {
			m++;
		} else if (ci > mi) {
			c++;
		}
	}

	if (m > c) {
		Log("Mishka");
	} else if (c > m) {
		Log("Chris");
	} else {
		Log("Friendship is magic!^^");
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
