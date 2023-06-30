#include <iostream>
#include <string>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	string s1, s2;
	cin >> s1 >> s2;

	for (int i = 0; i < s1.length(); i++) {
		if (s1[i] == s2[i]) {
			cout << 0;
		} else {
			cout << 1;
		}
	}
	cout << endl;
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
