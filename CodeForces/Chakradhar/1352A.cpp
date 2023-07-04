#include <iostream>
#include <array>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	long n, k = 1, cnt = 0;
	cin >> n;

	array<int, 5> a{};

	for (auto it = a.begin(); it != a.end(); it++) {
		*it = n % 10;
		n /= 10;
	}

	for (auto& it: a) {
		if (it) {
			cnt++;
		}

		it *= k;
		k *= 10;
	}

	Log(cnt);
	for (auto& it: a) {
		if (it == 0) {
			continue;
		}

		cout << it << " ";
	}
	cout << endl;
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
