#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int a, b;
	cin >> a >> b;

	int side = (a < b) ? a : b;
	side *= 2;
	int max = (a > b) ? a : b;

	side = (side > max) ? side : max;

	Log((side * side));

}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
