#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n;
	cin >> n;

	vector<int> s;
	s.resize(n);

	for (int i = 0; i < n; i++) {
		cin >> s[i];
	}
	sort(s.begin(), s.end());

	int mindiff = s[n-1] - s[0] + 1;
	for (int i = 0; i < n-1; i++) {
		if ((s[i+1] - s[i]) <= mindiff) {
			mindiff = s[i+1] - s[i];
		}
	}

	Log(mindiff);
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
