#include <iostream>
#include <string>
#include <set>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	string name;
	cin >> name;

	set<char> unique;

	for (char c : name) {
		unique.insert(c);
	}

	if (unique.size() % 2) {
		Log("IGNORE HIM!");
	} else {
		Log("CHAT WITH HER!");
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
