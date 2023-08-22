#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, x;
	cin >> n;
	long expenses, sum = 0;

	int max = -1;
	for (int i = 0; i < n; i++) {
		cin >> x;
		sum += x;
		if (x > max) {
			max = x;
		}
	}

	expenses = (n * max) - sum;

	Log(expenses);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
