#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int k, n, w;
	cin >> k >> n >> w;

	int sum = (w * (w + 1)) / 2;
	sum *= k;

	sum -= n;
	Log((sum > 0 ? sum : 0));
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
