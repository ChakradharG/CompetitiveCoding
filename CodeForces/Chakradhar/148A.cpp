#include <iostream>
#include <numeric>
using namespace std;
#define Log(x) cout << x << "\n"

// void func() {
// 	int k, l, m, n, d, count = 0;
// 	cin >> k >> l >> m >> n >> d;
 
// 	for (int i = 1; i <= d; i++) {
// 		if (
// 			!(i % k) ||
// 			!(i % l) ||
// 			!(i % m) ||
// 			!(i % n)
// 		) {
// 			count++;
// 		}
// 	}
 
// 	Log(count);
// }

void func() {
	unsigned long k, l, m, n, d, count = 0;
	cin >> k >> l >> m >> n >> d;

	count += (d / k);
	count += (d / l);
	count += (d / m);
	count += (d / n);

	unsigned long kl = lcm(k, l), 
		km = lcm(k, m), 
		kn = lcm(k, n), 
		lm = lcm(l, m), 
		ln = lcm(l, n), 
		mn = lcm(m, n);
	count -= (d / kl);
	count -= (d / km);
	count -= (d / kn);
	count -= (d / lm);
	count -= (d / ln);
	count -= (d / mn);

	unsigned long klm = lcm(kl, m), 
		kln = lcm(kl, n), 
		kmn = lcm(km, n), 
		lmn = lcm(lm, n);
	count += (d / klm);
	count += (d / kln);
	count += (d / kmn);
	count += (d / lmn);

	unsigned long klmn = lcm(klm, n);
	count -= (d / klmn);

	Log(count);
}

int main() {
	ios::sync_with_stdio(false);
	func();
}
