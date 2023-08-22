#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int a, b, c, d;
	cin >> a >> b >> c >> d;

	int sum = ((b > a) ? 1 : 0) +
			((c > a) ? 1 : 0) +
			((d > a) ? 1 : 0);

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
