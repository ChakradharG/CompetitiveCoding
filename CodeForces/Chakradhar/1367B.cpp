#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, par = 0, odd = 0;
	cin >> n;

	vector<int> a;
	a.resize(n);
	for (int i = 0; i < n; i++)  {
		cin >> a[i];
		if (a[i] % 2) {
			odd++;
			if (!(i % 2)) {
				par++;
			}
		}
	}

	if (odd != n / 2) {
		Log(-1);
	} else {
		Log(par);
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
