#include <iostream>
#include <string>
#include <set>
using namespace std;
#define Log(x) cout << x << "\n"

bool distinct(string y) {
	set<char> digits;

	for (char c: y) {
		digits.insert(c);
	}

	return (digits.size() == y.length());
}

void func() {
	string y;
	cin >> y;
	int n = y.length();
	int year = stoi(y);
	y = to_string(++year);

	while (!distinct(y)) {
		year = stoi(y);
		y = to_string(++year);
	}

	Log(y);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
