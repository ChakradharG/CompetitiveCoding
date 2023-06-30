#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, p;
	cin >> n;

	int* count = new int[n]();

	for (int i = 0; i < n; i++) {
		cin >> p;
		count[p-1] = i + 1;
	}

	for (int i = 0; i < n; i++) {
		cout << count[i] << " ";
	}
	cout << endl;
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
