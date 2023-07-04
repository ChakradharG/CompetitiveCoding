#include <iostream>
#include <array>
#include <string>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	string s1, s2, s3;
	cin >> s1 >> s2 >> s3;

	array<int, 26> arr{};

	for (char c: s3) {
		arr[c - 65]++;
	}

	for (char c: (s1 + s2)) {
		arr[c - 65]--;
	}

	for (auto& it: arr) {
		if (it != 0) {
			Log("NO");
			return;
		}
	}
	Log("YES");
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
