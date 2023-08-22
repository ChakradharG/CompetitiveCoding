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

	int last = a[n-1];
	for (int i = n-1; i > 0; i--) {
		a[i] -= a[i-1];
	}
	a[0] -= last;

	int index = -1;
	for (int i = 0; i < n-1; i++) {
		if ((a[i] != 0) && (a[i+1] != 0)) {
			index = i;
			break;
		}
	}
	if (index == -1) {
		index = n-1;
	}

	Log((index+1));
	
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
