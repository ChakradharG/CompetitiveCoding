#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, m;
	cin >> n >> m;

	string s0, s1, s2;
	s0 = string(m, '#');
	s1 = string(m, '.');
	s2 = string(m, '.');

	s1[s1.length()-1] = '#';
	s2[0] = '#';

	for (int i = 0; i < n; i++) {
		if (!(i % 2)) {
			Log(s0);
		} else {
			if ((i % 4) == 1) {
				Log(s1);
			} else {
				Log(s2);
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
