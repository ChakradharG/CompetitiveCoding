#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	unsigned long long n;
	cin >> n;

	int count = 0;
	count += (n / 100);
	n %= 100;
	count += (n / 20);
	n %= 20;
	count += (n / 10);
	n %= 10;
	count += (n / 5);
	n %= 5;
	count += n;

	Log(count);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
