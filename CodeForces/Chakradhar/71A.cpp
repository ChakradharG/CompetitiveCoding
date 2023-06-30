#include <iostream>
#include <string>
using namespace std;
#define Log(x) cout << x << "\n"

void func(){
	int n;
	string s;

	cin >> n;
	while (n--) {
		cin >> s;
		if (s.length() > 10) {
			cout << s.at(0) << s.length() - 2 << s.at(s.length() - 1) << "\n";
		} else {
			Log(s);
		}
	}
}

int main(){
	func();
}