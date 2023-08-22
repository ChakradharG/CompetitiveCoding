#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, k, x;
	cin >> n >> k;
	int eligible = 0;

	while (n--) {
		cin >> x;
		if ((5 - x) >= k) {
			eligible++;
		}
	}

	Log((eligible / 3));
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
