#include <iostream>
#include <set>
using namespace std;
#define Log(x) cout << x << "\n"

void func() {
	unsigned long s1, s2, s3, s4;
	cin >> s1 >> s2 >> s3 >> s4;

	set<unsigned long> colors;
	colors.insert(s1);
	colors.insert(s2);
	colors.insert(s3);
	colors.insert(s4);

	int s = 4 - colors.size();

	Log(s);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
