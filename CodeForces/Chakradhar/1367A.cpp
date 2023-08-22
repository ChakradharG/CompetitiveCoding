#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	string a, b;
	cin >> b;

	for (int i = 0; i < b.length(); i += 2) {
		a = a + b[i];
	}
	a = a + b[b.length()-1];

	Log(a);
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
