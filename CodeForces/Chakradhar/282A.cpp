#include <iostream>
#include <string>
using namespace std;
#define Log(x) cout << x << "\n"

void func(){
	int n, x = 0;
	cin >> n;
	string s;

	while (n--) {
		cin >> s;
		if (s.find('+') != std::string::npos) {
			x++;
		} else {
			x--;
		}
	}

	Log(x);
}

int main(){
	ios::sync_with_stdio(false);
	func();
}