#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n;
	cin >> n;

	bool f = true;
	for (int i = 0; i < n; i++) {
		if (f) {
			cout << "I hate ";
		} else {
			cout << "I love ";
		}
		f = !f;

		if (i != (n-1)) {
			cout << "that ";
		} else {
			cout << "it" << endl;
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
