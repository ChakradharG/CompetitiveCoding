#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int a, b, diff;
	cin >> a >> b;
	diff = abs(a - b) + 9;
	Log((diff / 10));
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
