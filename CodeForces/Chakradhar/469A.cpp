#include <iostream>
#include <vector>
#include <numeric>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, p, q, j;
	cin >> n;

	vector<int> arr;
	arr.resize(n);

	cin >> p;
	for (int i = 0; i < p; i++) {
		cin >> j;
		arr[j-1] = 1;
	}

	cin >> q;
	for (int i = 0; i < q; i++) {
		cin >> j;
		arr[j-1] = 1;
	}

	if (n == accumulate(arr.begin(), arr.end(), 0)) {
		Log("I become the guy.");
	} else {
		Log("Oh, my keyboard!");
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
