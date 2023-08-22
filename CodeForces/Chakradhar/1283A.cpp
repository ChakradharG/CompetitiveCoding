#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int h, m;
	cin >> h >> m;

	int time = 0;
	time += (23 - h) * 60;
	time += (60 - m);
	Log(time);
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
