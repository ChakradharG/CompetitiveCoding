#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n;
	cin >> n;

	int c1 = n / 3, c2 = n / 3;
	if (n % 3 == 1) c1++;
	else if (n % 3 == 2) c2++;

	cout << c1 << " " << c2 << endl;
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
