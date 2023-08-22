#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, x;
	cin >> n;

	vector<int> a;
	for (int i = 0; i < n; i++) {
		cin >> x;
		a.push_back(x);
	}

	sort(a.begin(), a.end());

	for (int i = 0; i < n-1; i++) {
		if ((a[i+1] - a[i]) > 1) {
			Log("NO");
			return;
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
