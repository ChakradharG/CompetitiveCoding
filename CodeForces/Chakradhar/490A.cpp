#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int n, x;
	cin >> n;

	vector<int> t1, t2, t3;
	for (int i = 1; i < n+1; i++) {
		cin >> x;
		switch (x) {
		case 1:
			t1.push_back(i);
			break;
		case 2:
			t2.push_back(i);
			break;
		case 3:
			t3.push_back(i);
			break;
		}
	}

	int min = (t1.size() < t2.size()) ? t1.size() : t2.size();
	min = (min < t3.size()) ? min : t3.size();

	Log(min);
	for (int i = 0; i < min; i++) {
		cout << t1[i] << " " << t2[i] << " " << t3[i] << endl;
	}
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
