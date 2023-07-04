#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int a, b;
	cin >> a >> b;

	int c1, c2;
	if (a < b) {
		c1 = a;
		b -= a;
		c2 = b / 2;
	} else if (b < a) {
		c1 = b;
		a -= b;
		c2 = a / 2;
	} else {
		c1 = a;
		c2 = 0;
	}
	cout << c1 << " " << c2 << endl;
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
