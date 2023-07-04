#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	long n, count = 0, curr = 0, x;
	cin >> n;

	while (n--) {
		cin >> x;
		if (x == -1) {
			if (curr == 0) {
				count++;
			} else {
				curr--;
			}
		} else {
			curr += x;
		}
	}
	Log(count);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
