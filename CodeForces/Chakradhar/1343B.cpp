#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	long n;
	cin >> n;

	if (n % 4) {
		Log("NO");
	} else {
		Log("YES");
		int j = 2;
		for (int i = 0; i < n / 2; i++) {
			cout << j << " ";
			j += 2;
		}
		j = 1;
		for (int i = 0; i < n / 4; i++) {
			cout << j << " ";
			j += 2;
		}
		j += 2;
		for (int i = 0; i < n / 4; i++) {
			cout << j << " ";
			j += 2;
		}
		cout << endl;
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
