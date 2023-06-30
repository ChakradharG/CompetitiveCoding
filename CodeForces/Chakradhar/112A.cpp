#include <iostream>
#include <string>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int result;
	string one, two;
	bool broke = false;
	cin >> one;
	cin >> two;

	for (int i = 0; i < one.length(); i++) {
		result = tolower(one[i]) - tolower(two[i]);
		if (result) {
			Log(((result < 0) ? -1 : 1));
			broke = true;
			break;
		}
	}

	if (!broke) {
		Log(0);
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
