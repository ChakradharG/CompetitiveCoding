#include <iostream>
#include <vector>
using namespace std;
#define Log(x) cout << x << "\n"

void func(){
	int n, n2, k, a, total = 0;
	vector<int> v;
	cin >> n >> k;

	n2 = n;

	while (n2--) {
		cin >> a;
		v.push_back(a);
	}

	int kth = v[k-1];
	

	for (int i = 0; i < n; i++) {
		if ((v[i] >= kth) && (v[i] > 0)) {
			total++;
		}
	}

	Log(total);
}

int main(){
	ios::sync_with_stdio(false);
	func();
}