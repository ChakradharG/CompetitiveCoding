#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	long n;
	cin >> n;

	long max = n - 1, min = (n / 2) + 1;

	Log((max - min + 1));
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
