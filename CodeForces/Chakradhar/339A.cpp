#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	string sum;
	cin >> sum;

	vector<int> summands;
	for (int i = 0; i < sum.length(); i += 2) {
		summands.push_back(sum[i] - '0');
	}
	sort(summands.begin(), summands.end());

	for (int i = 0; i < summands.size()-1; i++) {
		cout << summands[i] << "+";
	}
	cout << summands[summands.size()-1] << endl;
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
