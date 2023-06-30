#include <iostream>
#include <vector>
#include <string>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, count = 0;
	cin >> n;

	vector<char> stones;
	stones.resize(n);
	cin >> stones[0];
	char last = stones[0];
	for (int i = 1; i < n; i++) {
		cin >> stones[i];
		if (stones[i] == last) {
			count++;
		}
		else {
			last = stones[i];
		}
	}

	Log(count);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
