#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int a, b, c;
	cin >> a >> b >> c;

	if ((a + b) == c) {
		Log("+");
	} else {
		Log("-");
	}
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
