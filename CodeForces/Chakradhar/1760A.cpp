#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	array<int, 3> a;
	cin >> a[0] >> a[1] >> a[2];
	sort(a.begin(), a.end());

	Log(a[1]);
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
