#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func(){
	int n, total = 0;
	cin >> n;
	int p, v, t;

	while (n--) {
		cin >> p >> v >> t;

		if ((p + v + t) > 1) {
			total++;
		}
	}

	Log(total);
}

int main(){
	ios::sync_with_stdio(false);
	func();
}