#include <iostream>
#include <string>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, A = 0, D = 0;
	string games;
	cin >> n >> games;

	for (char game: games) {
		if (game == 'A') {
			A++;
		} else {
			D++;
		}
	}

	if (A > D) {
		Log("Anton");
	} else if (D > A) {
		Log("Danik");
	} else {
		Log("Friendship");
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
