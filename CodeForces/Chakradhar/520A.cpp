#include <iostream>
#include <string>
#include <vector>
#include <numeric>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n;
	cin >> n;

	vector<int> alphabets;
	alphabets.resize(26);

	string s;
	cin >> s;
	for (char c: s) {
		if (c > 96) {
			alphabets[c - 97] = 1;
		} else {
			alphabets[c - 65] = 1;
		}
	}

	int count = accumulate(alphabets.begin(), alphabets.end(), 0);
	if (count == 26) {
		Log("YES");
	} else {
		Log("NO");
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
