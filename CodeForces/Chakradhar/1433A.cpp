	#include <bits/stdc++.h>
	using namespace std;
	#define Log(x) cout << x << "\n"
	
	void func() {
		string x;
		cin >> x;

		int key = (x[0] - 49) * 10;
		int n = x.length();
		key += n*(n+1)/2;

		Log(key);
	}
	
	int main() {
		ios::sync_with_stdio(false);
		int t;
		cin >> t;
		while (t-- > 0){
			func();
		}
	}
	