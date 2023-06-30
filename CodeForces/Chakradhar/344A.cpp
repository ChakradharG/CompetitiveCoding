#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, group = 1;
	cin >> n;
	char c1, c2;
	cin >> c1 >> c2;
	n--;

	while (n--) {
		cin >> c1;
		if (c2 == c1) {
			group++;
		}
		cin >> c2;
	}

	Log(group);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
