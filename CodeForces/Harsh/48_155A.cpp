#include <iostream>
using namespace std;
int main()
{
    int m, point;
    cin >> m;
    int amazing = 0;
    cin >> point;
    int max = point, min = point;
    m--;
    while (m--) {
        cin >> point;
        if (point < min) {
            amazing++;
            min = point;
        }
        else if (point > max) {
            amazing++;
            max = point;
        }
    }
    
    cout << amazing;
}