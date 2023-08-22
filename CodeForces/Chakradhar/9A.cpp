#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int y, w;
	cin >> y >> w;
	int max = (y > w) ? y : w;

	switch (max) {
		case 1:
			Log("1/1");
			break;
		case 2:
			Log("5/6");
			break;
		case 3:
			Log("2/3");
			break;
		case 4:
			Log("1/2");
			break;
		case 5:
			Log("1/3");
			break;
		case 6:
			Log("1/6");
			break;
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
