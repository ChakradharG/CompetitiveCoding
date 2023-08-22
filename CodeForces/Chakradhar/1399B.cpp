#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, ma, mb;
	cin >> n;
	vector<int> a, b;
	a.resize(n);
	b.resize(n);

	cin >> a[0];
	ma = a[0];
	for (int i = 1; i < n; i++) {
		cin >> a[i];
		if (ma > a[i]) ma = a[i];
	}

	cin >> b[0];
	mb = b[0];
	for (int i = 1; i < n; i++) {
		cin >> b[i];
		if (mb > b[i]) mb = b[i];
	}

	unsigned long long sum = 0;
	for (int i = 0; i < n; i++) {
		sum += max(a[i]-ma, b[i]-mb);
	}

	Log(sum);
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
