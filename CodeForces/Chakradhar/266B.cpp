#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, k;
	cin >> n >> k;
	string s;

	cin >> s;
	while (k--) {
		int i = 0;
		while (i < n-1) {
			if ((s[i] == 'B') && (s[i+1] == 'G')) {
				s[i] = 'G';
				s[i+1] = 'B';
				i += 2;
			} else {
				i++;
			}
		}
	}

	Log(s);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
