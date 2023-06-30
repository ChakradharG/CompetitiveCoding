#include <iostream>
#include <string>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	string s;
	cin >> s;
	cout << char(toupper(s[0]));
	for (int i = 1; i < s.length(); i++) {
		cout << s[i];
	}
	cout << endl;
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
