#include <iostream>
#include <numeric>
#include <vector>
#include <string>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	string s;
	getline(cin, s);
	vector<int> arr;
	arr.resize(26);

	s = s.substr(1, s.length()-2);
	for (char c: s) {
		if (c >= 65 && c <= 90) {
			arr[c-65] = 1;
		} else if (c >= 97 && c <= 122) {
			arr[c-97] = 1;
		}
	}

	Log(accumulate(arr.begin(), arr.end(), 0));
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
