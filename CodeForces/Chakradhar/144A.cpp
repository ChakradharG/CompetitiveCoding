#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, val, res;
	cin >> n;

	int max = 0, min = 101, max_ind = -1, min_ind = -1;
	for (int i = 0; i < n; i++) {
		cin >> val;
		if (val > max) {
			max = val;
			max_ind = i;
		}
		if (val <= min) {
			min = val;
			min_ind = i;
		}
	}

	res = max_ind + (n - (min_ind + 1));

	if (max_ind > min_ind) {
		res--;
	}

	Log(res);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
