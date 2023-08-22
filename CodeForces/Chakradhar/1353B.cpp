#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, k;
	cin >> n >> k;

	vector<int> a, b, c;
	a.resize(n);
	b.resize(n);
	c.resize(n+k);

	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	for (int i = 0; i < n; i++) {
		cin >> b[i];
	}

	sort(a.begin(), a.end());
	sort(b.begin(), b.end());

	copy(a.begin(), a.end(), c.begin());
	copy(b.end()-k, b.end(), c.begin()+n);

	sort(c.begin(), c.end());
	
	Log(accumulate(c.begin()+k, c.end(), 0));
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
