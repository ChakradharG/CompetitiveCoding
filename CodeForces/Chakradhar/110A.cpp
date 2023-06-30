#include <iostream>
#include <string>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	string n;
	cin >> n;

	int count_lucky = 0, num, mod;
	bool lucky = false;

	for (char c: n) {
		num = c - 48;
		if ((num == 4) || (num == 7)) {
			count_lucky++;
		}
	}

	while (count_lucky) {
		mod = count_lucky % 10;
		count_lucky /= 10;

		if ((mod != 4) && (mod != 7)) {
			lucky = false;
			break;
		} else {
			lucky = true;
		}
	}

	if (lucky) {
		Log("YES");
	} else {
		Log("NO");
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
