#include <iostream>
#include <string>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	string s, s_lower, s_upper;
	cin >> s;

	s_lower = s;
	s_upper = s;

	int change_lower = 0, change_upper = 0;

	for (int i = 0; i < s.length(); i++) {
		s_lower[i] = tolower(s[i]);
		if (s[i] != s_lower[i]) {
			change_lower++;
		}
		s_upper[i] = toupper(s[i]);
		if (s[i] != s_upper[i]) {
			change_upper++;
		}
	}

	if (change_upper < change_lower) {
		Log(s_upper);
	} else {
		Log(s_lower);
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
