#include <iostream>
#include <cstdlib>
using namespace std;
 
int main() {
    // Write C++ code here
    int price, burle;
    cin >> price >> burle;
    int count = 1;
    int op = price;
    while (true) {
        if ((price % 10 == 0) || ((price - burle)%10 == 0)) break;
        else {
            price += op;
            count++;
        }
    }
    cout << count;
}