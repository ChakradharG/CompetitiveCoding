#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func(){
	int row = 1, col = 1;
	int x;

	while ((row <= 5) && (col <= 5)) {
		cin >> x;
		if (x == 1) {
			break;
		} else {
			col++;
			if (col > 5) {
				row++;
				col = 1;
			}
		}
	}

	Log(abs(row - 3) + abs(col - 3));
}

int main(){
	ios::sync_with_stdio(false);
	func();
}