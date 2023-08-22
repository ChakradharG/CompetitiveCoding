#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, x;
	cin >> n >> x;
	int max = x, min = x;
	for (int i = 1; i < n; i++) {
		cin >> x;
		if (max < x) max = x;
		if (min > x) min = x;
	}

	Log((max - min));
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
