#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int k, x = 0;
	cin >> k;

	int count = 0;
	while (count < k) {
		x++;
		if ((x % 3) && ((x % 10) != 3)) {
			count++;
		}
	}

	Log(x);
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
