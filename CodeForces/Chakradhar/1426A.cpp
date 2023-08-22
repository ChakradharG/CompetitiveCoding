#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, x, floor;
	cin >> n >> x;

	floor = 1;
	n -= 2;
	if (n < 0) n = 0;
	floor += n / x;

	if (n % x) floor++;

	Log(floor);
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
