#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int s1, s2, s3, s4;
	cin >> s1 >> s2 >> s3 >> s4;

	int min = (s1 < s2) ? s1 : s2;
	int max = (s3 > s4) ? s3 : s4;

	if (max < min) {
		Log("NO");
		return;
	}

	min = (s3 < s4) ? s3 : s4;

	max = (s1 > s2) ? s1 : s2;
	if (max < min) {
		Log("NO");
		return;
	}

	Log("YES");
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
