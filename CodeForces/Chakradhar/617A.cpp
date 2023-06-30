#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int x;
	cin >> x;

	int steps = 0;

	steps += x / 5;
	x %= 5;

	steps += x / 4;
	x %= 4;

	steps += x / 3;
	x %= 3;

	steps += x / 2;
	x %= 2;

	steps += x;

	Log(steps);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
