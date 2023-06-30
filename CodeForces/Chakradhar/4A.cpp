#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func(){
	int w;
	cin >> w;

	if (w % 2 == 0 && w > 2) {
		Log("YES");
	} else {
		Log("NO");
	}
}

int main(){
	ios::sync_with_stdio(false);
	func();
}