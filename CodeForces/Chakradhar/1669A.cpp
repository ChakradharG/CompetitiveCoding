#include <bits/stdc++.h>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	int rating;
	cin >> rating;

	if (1900 <= rating) {
		Log("Division 1");
	} else if (1600 <= rating && rating <= 1899) {
		Log("Division 2");
	} else if (1400 <= rating && rating<= 1599) {
		Log("Division 3");
	} else if (rating <= 1399) {
		Log("Division 4");
	}
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	while (t-- > 0){
		func();
	}
}
