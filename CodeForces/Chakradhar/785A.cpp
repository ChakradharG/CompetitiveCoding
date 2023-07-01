#include <iostream>
#include <string>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	unsigned long n, count = 0;
	cin >> n;

	string s;
	while (n--) {
		cin >> s;

		if (s == "Tetrahedron") {
			count += 4;
		} else if (s == "Cube") {
			count += 6;
		} else if (s == "Octahedron") {
			count += 8;
		} else if (s == "Dodecahedron") {
			count += 12;
		} else if (s == "Icosahedron") {
			count += 20;
		}
	}

	Log(count);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
