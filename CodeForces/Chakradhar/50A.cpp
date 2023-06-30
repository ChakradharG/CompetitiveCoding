#include <iostream>
using namespace std;
#define Log(x) cout << x << "\n"

void func(){
	int M, N;
	cin >> M >> N;

	int total = (M * N) / 2;

	Log(total);
}

int main(){
	ios::sync_with_stdio(false);
	func();
}