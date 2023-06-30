#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, p;
	cin >> n;

	double p_total = 0;
	for (int i = 0; i < n; i++) {
		cin >> p;
		p_total += p;
	}

	Log(p_total/n);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
