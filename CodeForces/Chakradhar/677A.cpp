#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, h;
	cin >> n >> h;

	int sum = 0, p;
	while (n--) {
		cin >> p;
		sum += ((p > h) ? 2 : 1);
	}

	Log(sum);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
