#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, eh;
	cin >> n;

	while (n--) {
		cin >> eh;
		if (eh == 1) {
			Log("HARD");
			return;
		}
	}

	Log("EASY");
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
