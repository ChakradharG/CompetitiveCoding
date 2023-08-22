#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

bool isprime(int x) {
	if (x % 2 == 0) {
		if (x == 2) {
			return true;
		} else {
			return false;
		}
	} else {
		for (int i = 3; i <= round(sqrt(x)); i += 2) {
			if (x % i == 0) {
				return false;
			}
		}
		return true;
	}
}

void func() {
	int n, m;
	cin >> n >> m;

	if (isprime(m)) {
		for (int i = n+1; i < m; i++) {
			if(isprime(i)) {
				Log("NO");
				return;
			}
		}
		Log("YES");
	} else {
		Log("NO");
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
